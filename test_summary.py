
import requests

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

print("FraudShield Automated Test Report\n")

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
                print(f"Test {number}: PASS - {prediction}")
            else:
                failed += 1
                print(f"Test {number}: FAIL - Invalid prediction")
        else:
            failed += 1
            print(f"Test {number}: FAIL - HTTP {response.status_code}")

    except requests.exceptions.RequestException:
        failed += 1
        print(f"Test {number}: FAIL - Request error")

print("\n========== FINAL SUMMARY ==========")
print("Total tests:", total)
print("Passed:", passed)
print("Failed:", failed)

if failed == 0:
    print("Overall result: ALL TESTS PASSED")
else:
    print("Overall result: SOME TESTS FAILED")
