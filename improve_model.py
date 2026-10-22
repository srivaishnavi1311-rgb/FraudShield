
import pandas as pd
import joblib

from sklearn.tree import DecisionTreeClassifier

# Create boundary-focused practice data
data = {
    "amount": [
        1000, 2000, 10000, 25000, 40000,
        49999, 50000, 50001, 60000, 80000,
        1000, 2000, 3000, 4000, 5000
    ],
    "international_number": [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1
    ],
    "status": [
        0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
}

df = pd.DataFrame(data)

X = df[["amount", "international_number"]]
y = df["status"]

# Train a new, deeper decision tree
model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X, y)

# Save as a separate model file
joblib.dump(model, "fraudshield_improved_model.joblib")

print("Improved practice model trained and saved!")
print("Training records:", len(df))
print("Saved as: fraudshield_improved_model.joblib")
