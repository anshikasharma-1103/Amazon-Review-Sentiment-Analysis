import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("dataset/AMAZON_FASHION_5_part0.csv")

# ==========================
# Keep Required Columns
# ==========================
df = df[["reviewText", "overall"]]

# ==========================
# Remove Missing Values
# ==========================
df.dropna(inplace=True)

# Remove Empty Reviews
df = df[df["reviewText"].str.strip() != ""]

# ==========================
# Create Sentiment Column
# ==========================
def get_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating <= 2:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["overall"].apply(get_sentiment)

# Remove Neutral Reviews
df = df[df["sentiment"] != "Neutral"]

# ==========================
# Features and Labels
# ==========================
X = df["reviewText"]
y = df["sentiment"]

# ==========================
# Convert Text into Numbers
# ==========================
vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True,
)

X = vectorizer.fit_transform(X)

# ==========================
# Split Dataset
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================
# Train Model
# ==========================
model = MultinomialNB()
model.fit(X_train, y_train)

# ==========================
# Make Predictions
# ==========================
y_pred = model.predict(X_test)

# ==========================
# Calculate Accuracy
# ==========================
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("MODEL ACCURACY")
print("=" * 50)

print(f"Accuracy : {accuracy*100:.2f}%")

# ==========================
# Classification Report
# ==========================
print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# ==========================
# Confusion Matrix
# ==========================
print("Confusion Matrix\n")
print(confusion_matrix(y_test, y_pred))

# ==========================
# Save Model
# ==========================
joblib.dump(model, "review_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel Saved Successfully!")
print("review_model.pkl")
print("vectorizer.pkl")