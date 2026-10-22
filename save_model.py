
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the synthetic dataset
df = pd.read_csv("synthetic_transactions.csv")

X = df[["amount", "international_number"]]
y = df["status"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train the model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "fraudshield_model.joblib")

print("Model saved successfully!")

# Load the saved model
loaded_model = joblib.load("fraudshield_model.joblib")

# Predict a new transaction
new_transaction = pd.DataFrame({
    "amount": [20000],
    "international_number": [0]
})

prediction = loaded_model.predict(new_transaction)[0]

print("Prediction:", "SUSPICIOUS" if prediction == 1 else "LOW RISK")
