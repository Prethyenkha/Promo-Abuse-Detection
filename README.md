
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

## 📸 App Preview

### 🔹 Upload CSV Page

<img width="1365" height="604" alt="Screenshot 2025-08-05 141120" src="https://github.com/user-attachments/assets/db403104-5130-49ec-bc61-4a84d2bcc3a5" />

### 🔹 Risk Level Output

<img width="1361" height="618" alt="Screenshot 2025-08-05 141155" src="https://github.com/user-attachments/assets/6ff37206-d065-40a3-86f0-ba4f482a2ebe" />

---
