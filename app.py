from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import pandas as pd
import joblib
from scipy.cluster.hierarchy import linkage, fcluster
import traceback

app = Flask(__name__)
app.secret_key = 'promo_abuse_secret'

# Load pre-trained scaler
scaler = joblib.load("hierarchical_scaler.pkl")
trained_features = scaler.feature_names_in_

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster', methods=['POST'])
def cluster():
    try:
        if 'file' not in request.files:
            flash("🚫 No file uploaded!", "danger")
            return redirect(url_for('index'))

        file = request.files['file']
        if file.filename == '':
            flash("⚠️ Please select a file.", "danger")
            return redirect(url_for('index'))

        # Read uploaded CSV
        df = pd.read_csv(file)

        # Keep only numeric columns
        numeric_df = df.select_dtypes(include=['int64', 'float64']).copy()

        # Add missing trained features as zeros
        for col in trained_features:
            if col not in numeric_df.columns:
                numeric_df[col] = 0

        # Reorder to match scaler
        numeric_df = numeric_df[trained_features]
        numeric_df.fillna(0, inplace=True)

        # Scale numeric data
        scaled_data = scaler.transform(numeric_df)

        # Perform hierarchical clustering
        linked = linkage(scaled_data, method='ward')

        # Assign clusters
        clusters = fcluster(linked, t=3, criterion='maxclust')
        df['Cluster'] = clusters

        # Map clusters to Risk Levels
        risk_map = {1: 'Low Risk', 2: 'Medium Risk', 3: 'High Risk'}
        df['Risk_Level'] = df['Cluster'].map(risk_map)

        # Combine First and Last Name for display
        df['Name'] = df['FirstName'] + ' ' + df['LastName']

        # Show only Name and Risk Level
        display_df = df[['Name', 'Risk_Level']].head(20)

        # Save full clustered output
        output_file = "Promo_Abuse_Clustered_Risk.csv"
        df.to_csv(output_file, index=False)

        # Prepare preview
        table_data = display_df.to_dict(orient='records')
        return render_template('results.html', table_data=table_data)

    except Exception as e:
        traceback.print_exc()
        flash(f"❌ Error: {str(e)}", "danger")
        return redirect(url_for('index'))

@app.route('/download')
def download():
    return send_file("Promo_Abuse_Clustered_Risk.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
