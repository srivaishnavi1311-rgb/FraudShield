import requests

API_URL = "http://127.0.0.1:8000/predict"

test_cases = [
    {
        "name": "Small domestic transaction",
        "data": {"amount": 500, "international": False},
        "expected_status": 200,
        "expected_prediction": "LOW RISK"
    },
    {
        "name": "Large domestic transaction",
        "data": {"amount": 60000, "international": False},
        "expected_status": 200,
        "expected_prediction": "SUSPICIOUS"
    },
    {
        "name": "International transaction",
        "data": {"amount": 2000, "international": True},
        "expected_status": 200,
        "expected_prediction": "SUSPICIOUS"
    },
    {
        "name": "Zero amount",
        "data": {"amount": 0, "international": False},
        "expected_status": 200,
        "expected_prediction": None
    },
    {
        "name": "Negative amount",
        "data": {"amount": -100, "international": False},
        "expected_status": 422,
        "expected_prediction": None
    },
    {
        "name": "Invalid Boolean string",
        "data": {"amount": 2000, "international": "yes"},
        "expected_status": 422,
        "expected_prediction": None
    }
]

passed = 0
failed = 0

for case in test_cases:
    try:
        response = requests.post(
            API_URL,
            json=case["data"],
            timeout=5
        )

        status_ok = (
            response.status_code == case["expected_status"]
        )

        prediction_ok = True

        if status_ok and response.status_code == 200:
            actual_prediction = response.json().get("prediction")

            if case["expected_prediction"] is not None:
                prediction_ok = (
                    actual_prediction == case["expected_prediction"]
                )

        if status_ok and prediction_ok:
            print(f'{case["name"]}: PASS')
            passed += 1
        else:
            print(f'{case["name"]}: FAIL')
            print(f'Expected status: {case["expected_status"]}')
            print(f'Received status: {response.status_code}')

            if response.status_code == 200:
                print("Actual prediction:", response.json().get("prediction"))

            failed += 1

    except (requests.RequestException, ValueError) as error:
        print(f'{case["name"]}: FAIL - {error}')
        failed += 1

print("\n===== TEST SUMMARY =====")
print(f"Total tests: {passed + failed}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")

if failed == 0:
    print("Overall result: ALL TESTS PASSED")
else:
    print("Overall result: SOME TESTS FAILED")