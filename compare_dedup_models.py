
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

# Compare the original and deduplicated datasets
datasets = {
    "Original Dataset": "synthetic_transactions.csv",
    "Deduplicated Dataset": "synthetic_transactions_deduplicated.csv"
}

for dataset_name, file_name in datasets.items():

    print("\n" + "=" * 45)
    print(dataset_name)
    print("=" * 45)

    # 1. Load dataset
    df = pd.read_csv(file_name)

    print("Total records:", len(df))

    # 2. Select features and target
    X = df[["amount", "international_number"]]
    y = df["status"]

    # 3. Split into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("Training records:", len(X_train))
    print("Testing records:", len(X_test))

    # 4. Create models
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

    # 5. Train and evaluate
    for model_name, model in models.items():

        model.fit(X_train, y_train)

        train_predictions = model.predict(X_train)
        test_predictions = model.predict(X_test)

        train_accuracy = accuracy_score(
            y_train, train_predictions
        )
        test_accuracy = accuracy_score(
            y_test, test_predictions
        )
        precision = precision_score(
            y_test, test_predictions, zero_division=0
        )
        recall = recall_score(
            y_test, test_predictions, zero_division=0
        )
        f1 = f1_score(
            y_test, test_predictions, zero_division=0
        )

        print("\nModel:", model_name)
        print(f"Training Accuracy: {train_accuracy:.3f}")
        print(f"Testing Accuracy:  {test_accuracy:.3f}")
        print(f"Precision:         {precision:.3f}")
        print(f"Recall:            {recall:.3f}")
        print(f"F1 Score:          {f1:.3f}")

        print("Confusion Matrix:")
        print(confusion_matrix(
            y_test, test_predictions, labels=[0, 1]
        ))

print("\nDataset comparison completed!")
