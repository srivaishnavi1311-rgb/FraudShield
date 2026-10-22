
import random
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)

# Make the practice data reproducible
random.seed(42)

# 1. Generate 1,000 synthetic transactions
transactions = []

for i in range(1000):
    amount = random.randint(100, 100000)
    international = random.choices(
        ["yes", "no"], weights=[15, 85]
    )[0]

    # Practice rule for generating labels
    if amount > 50000 or international == "yes":
        status = 1
    else:
        status = 0

    transactions.append({
        "amount": amount,
        "international": international,
        "status": status
    })

# 2. Create a DataFrame
df = pd.DataFrame(transactions)

# 3. Convert yes/no into numbers
df["international_number"] = df["international"].map({
    "no": 0,
    "yes": 1
})

# 4. Save the practice dataset
df.to_csv("synthetic_transactions.csv", index=False)

# 5. Select features and target
X = df[["amount", "international_number"]]
y = df["status"]

# 6. Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Total records:", len(df))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# 7. Train the model using training data only
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

# 8. Predict on unseen testing data
predictions = model.predict(X_test)

# 9. Evaluate the model
print("\n--- Model Evaluation ---")
print("Accuracy:", round(accuracy_score(y_test, predictions), 4))
print("Precision:", round(
    precision_score(y_test, predictions, zero_division=0), 4
))
print("Recall:", round(
    recall_score(y_test, predictions, zero_division=0), 4
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions, labels=[0, 1]))

print("\nPractice dataset saved successfully!")
