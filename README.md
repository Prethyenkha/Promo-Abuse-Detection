
# 🚨 Promo Abuse Detection App

## 📌 Overview
The **Promo Abuse Detection App** is a Flask-based web application that leverages **Hierarchical Clustering** to identify potential promo abuse by clustering users into different **risk levels** (Low, Medium, High).  
It provides an easy-to-use **dark-themed frontend** for uploading CSV files, visualizing results, and downloading the processed output.

---

## 🛠️ Tech Stack
- Python 3
- Flask
- Pandas, Scipy
- Joblib
- Bootstrap (Dark Theme)

---

## ✨ Features
- 📂 Upload CSV data containing user records
- 🔍 Automatically detects promo abuse clusters
- 🎨 Dark UI with color-coded risk levels
- 📥 Download clustered results
- 🛡️ `.gitignore` included to keep the repo clean

---

## 🚀 Installation

```bash
git clone https://github.com/Prethyenkha/Promo-Abuse-Detection.git
cd Promo-Abuse-Detection
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python app.py
```
Then, open your browser and go to:  
👉 `http://127.0.0.1:5000`

---

## 📝 Usage
1. Upload your dataset CSV.
2. Click **Cluster** to analyze.
3. View the **Name & Risk Level** in a clean table.
4. Download the processed file for further analysis.

---

## 📂 Project Structure

```
Promo Abuse Detection/
│── app.py
│── hierarchical_scaler.pkl
│── requirements.txt
│── templates/
│     ├── index.html
│     ├── results.html
│── static/
│── README.md
```

---

## 📸 Screenshots

### 🔹 Upload CSV Page
![Upload Page](screenshot-upload.png)

### 🔹 Risk Level Output
![Results Page](screenshot-results.png)

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 🛡️ License
Distributed under the MIT License.
