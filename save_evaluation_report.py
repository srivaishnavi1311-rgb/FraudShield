from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Practice example: 0 = LOW RISK, 1 = SUSPICIOUS
y_true = [0, 0, 1, 1, 1, 0]
y_pred = [0, 1, 1, 1, 0, 0]

# Calculate evaluation metrics
cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
accuracy = accuracy_score(y_true, y_pred)

report = classification_report(
    y_true,
    y_pred,
    labels=[0, 1],
    target_names=["LOW RISK", "SUSPICIOUS"],
    zero_division=0
)

# Prepare the report
report_text = f"""FRAUDSHIELD - MODEL EVALUATION REPORT
=====================================

Note: This is a practice example, not a real-world model evaluation.

Confusion Matrix:
{cm}

Accuracy: {accuracy * 100:.2f}%

Classification Report:
{report}
"""

# Save the report
with open("evaluation_report.txt", "w", encoding="utf-8") as file:
    file.write(report_text)

print("Evaluation report saved successfully!")
print(f"Accuracy: {accuracy * 100:.2f}%")