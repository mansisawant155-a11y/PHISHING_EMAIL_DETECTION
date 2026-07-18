import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


# =====================================
# LOAD DATASET
# =====================================

print("Loading dataset...")

df = pd.read_csv("phishing_email.csv")

print(df.head())


# =====================================
# CHECK MISSING VALUES
# =====================================

df.dropna(inplace=True)


# =====================================
# CONVERT LABELS
# safe = 0
# phishing = 1
# =====================================

df["Label"] = df["Label"].map({
    "safe": 0,
    "phishing": 1
})


# =====================================
# INPUT AND OUTPUT
# =====================================

X = df["Email"]
y = df["Label"]


# =====================================
# TF-IDF FEATURE EXTRACTION
# =====================================

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X = vectorizer.fit_transform(X)


# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =====================================
# TRAIN MODEL
# =====================================

print("\nTraining Model...")

model = MultinomialNB()

model.fit(X_train, y_train)


# =====================================
# PREDICTION
# =====================================

y_pred = model.predict(X_test)


# =====================================
# ACCURACY
# =====================================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy : {:.2f}%".format(accuracy * 100))


# =====================================
# CONFUSION MATRIX
# =====================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Safe", "Phishing"]
)

display.plot(cmap="Blues")

plt.title("Phishing Email Detection")
plt.show()


# =====================================
# SAVE MODEL
# =====================================

joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel Saved Successfully!")
print("phishing_model.pkl")
print("vectorizer.pkl")