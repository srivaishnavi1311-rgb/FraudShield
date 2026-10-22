
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    classification_report
)

# 0 = legitimate, 1 = fraud
actual = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
predicted = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]

print("Confusion Matrix:")
print(confusion_matrix(actual, predicted))

print("\nAccuracy:", accuracy_score(actual, predicted))
print("Precision:", precision_score(actual, predicted))
print("Recall:", recall_score(actual, predicted))

print("\nFull Report:")
print(classification_report(actual, predicted))
