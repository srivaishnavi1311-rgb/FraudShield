
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Actual labels: 0 = legitimate, 1 = fraudulent
actual =    [0, 0, 0, 0, 1, 1, 1, 1]
predicted = [0, 0, 1, 0, 1, 1, 0, 1]

# Calculate confusion matrix
matrix = confusion_matrix(actual, predicted, labels=[0, 1])

print("===== FraudShield Lesson 17 =====")
print("\nConfusion Matrix:")
print(matrix)

# Extract individual outcomes
tn, fp, fn, tp = matrix.ravel()

print("\nTrue Negatives:", tn)
print("False Positives:", fp)
print("False Negatives:", fn)
print("True Positives:", tp)

# Evaluate model
print("\nAccuracy:", round(accuracy_score(actual, predicted), 3))
print("Precision:", round(precision_score(actual, predicted), 3))
print("Recall:", round(recall_score(actual, predicted), 3))
