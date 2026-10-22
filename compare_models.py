
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# 1. Load the dataset
df = pd.read_csv("synthetic_transactions.csv")

print("===== FraudShield Model Comparison =====")
print("Total records:", len(df))

# 2. Select input features and target
X = df[["amount", "international_number"]]
y = df["status"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# 4. Create two models
models = {
    "Decision Tree": DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    ),
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000)
    )
}

# 5. Train and evaluate each model
for name, model in models.items():
    print("\n==============================")
    print("Model:", name)
    print("==============================")

    model.fit(X_train, y_train)

    # Evaluate on training data
    train_predictions = model.predict(X_train)
    train_accuracy = accuracy_score(y_train, train_predictions)

    # Evaluate on unseen test data
    predictions = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, predictions)

    print(f"Training Accuracy: {train_accuracy:.3f}")
    print(f"Testing Accuracy:  {test_accuracy:.3f}")
    precision = precision_score(
        y_test, predictions, zero_division=0
    )
    recall = recall_score(
        y_test, predictions, zero_division=0
    )
    f1 = f1_score(
        y_test, predictions, zero_division=0
    )

    print(f"Accuracy:  {test_accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall:    {recall:.3f}")
    print(f"F1 Score:  {f1:.3f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    if name == "Decision Tree":
        print("\nFeature Importance:")

        for feature, importance in zip(
            X.columns,
            model.feature_importances_
        ):
            print(f"{feature}: {importance:.3f}")

print("\nModel comparison completed!")
