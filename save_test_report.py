
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000/predict"

transactions = [
    {"amount": 2000, "international": False},
    {"amount": 2000, "international": True},
    {"amount": 60000, "international": False},
    {"amount": 1000, "international": False},
]

allowed_predictions = ["LOW RISK", "SUSPICIOUS"]

total = 0
passed = 0
failed = 0

report_lines = [
    "FraudShield Automated Test Report",
    "=" * 35,
    "Date and time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    ""
]

for number, transaction in enumerate(transactions, start=1):
    total += 1

    try:
        response = requests.post(
            API_URL,
            json=transaction,
            timeout=3
        )

        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction")

            if prediction in allowed_predictions:
                passed += 1
                message = f"Test {number}: PASS - {prediction}"
            else:
                failed += 1
                message = f"Test {number}: FAIL - Invalid prediction"
        else:
            failed += 1
            message = f"Test {number}: FAIL - HTTP {response.status_code}"

    except requests.exceptions.RequestException:
        failed += 1
        message = f"Test {number}: FAIL - Request error"

    print(message)
    report_lines.append(message)

report_lines.extend([
    "",
    "FINAL SUMMARY",
    "=" * 35,
    f"Total tests: {total}",
    f"Passed: {passed}",
    f"Failed: {failed}",
    "Overall result: " + (
        "ALL TESTS PASSED" if failed == 0
        else "SOME TESTS FAILED"
    )
])

report_text = "\n".join(report_lines)

with open("fraudshield_test_report.txt", "w", encoding="utf-8") as file:
    file.write(report_text)

print("\nReport saved to fraudshield_test_report.txt")
