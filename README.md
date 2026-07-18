# 🛡️ Phishing Email Detection Model

A Machine Learning-based web application that detects whether an email is **Phishing** or **Safe** using **Scikit-learn**, **Flask**, and **TF-IDF Vectorization**.

---

## 📌 Project Overview

Phishing emails are fraudulent emails designed to steal sensitive information such as passwords, banking details, and personal data.

This project uses a **Machine Learning model** trained on phishing and legitimate emails to classify user-entered email content as either:

- ✅ Safe
- ⚠️ Phishing

---

## 🚀 Features

- Detects phishing emails using Machine Learning
- TF-IDF feature extraction
- Multinomial Naive Bayes classifier
- Displays prediction result
- Displays confidence score
- Shows model accuracy
- Confusion Matrix visualization
- Modern Cybersecurity-themed UI
- Responsive Design

---

## 🛠 Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## 📂 Project Structure

```
Phishing_Email_Detection/
│
├── app.py
├── model.py
├── phishing_email.csv
├── phishing_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates/
│      └── index.html
│
└── static/
       ├── style.css
       └── script.js
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Phishing_Email_Detection.git
```

### 2. Open Project

```bash
cd Phishing_Email_Detection
```

### 3. Install Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run:

```bash
python model.py
```

This will generate:

- phishing_model.pkl
- vectorizer.pkl

---

## ▶️ Run Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

```
Dataset
      ↓
Data Cleaning
      ↓
TF-IDF Vectorization
      ↓
Train/Test Split
      ↓
Multinomial Naive Bayes
      ↓
Prediction
      ↓
Accuracy
      ↓
Confusion Matrix
```

---

## 📊 Algorithm Used

**Multinomial Naive Bayes**

Why?

- Fast
- Lightweight
- Excellent for text classification
- Works well with TF-IDF features

---

## 📈 Model Evaluation

The project displays:

- Accuracy Score
- Confusion Matrix
- Prediction Confidence

---

## 📸 User Interface

The website includes:

- Cybersecurity Theme
- Neon Blue UI
- Glassmorphism Card
- Loading Animation
- Confidence Progress Bar
- Responsive Design

---

## 📋 Example Input

```
Congratulations!

You have won ₹10,00,000.

Click here to claim your prize.
```

### Output

```
Prediction:
Phishing

Confidence:
98%
```

---

## 👨‍💻 Developed By

**Manasi Uday Sawant**

B.Sc. Computer Science

Machine Learning Internship Project

---

## 📄 License

This project is created for educational and internship purposes.