
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score
)

# Known labels for a small practice example
# 0 = LOW RISK, 1 = SUSPICIOUS
y_true = [0, 0, 1, 1, 1, 0]
y_pred = [0, 1, 1, 1, 0, 0]

# Evaluate the predictions
cm = confusion_matrix(
    y_true, y_pred, labels=[0, 1]
)

accuracy = accuracy_score(y_true, y_pred)

print("\n--- Confusion Matrix ---")
print(cm)

print("\n--- Accuracy ---")
print(f"{accuracy * 100:.2f}%")

print("\n--- Classification Report ---")
print(
    classification_report(
        y_true,
        y_pred,
        labels=[0, 1],
        target_names=["LOW RISK", "SUSPICIOUS"],
        zero_division=0
    )
)
