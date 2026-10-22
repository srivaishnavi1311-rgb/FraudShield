
import requests

API_URL = "http://127.0.0.1:8000/predict"

passed = 0
failed = 0


def test_prediction(name, data, expected_status, expected_prediction=None):
    global passed, failed

    print(f"\nTesting: {name}")

    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=5
        )

        status_ok = response.status_code == expected_status
        prediction_ok = True

        actual_prediction = None

        if response.status_code == 200:
            actual_prediction = response.json().get("prediction")
            print("Actual prediction:", actual_prediction)

            if expected_prediction is not None:
                prediction_ok = (
                    actual_prediction == expected_prediction
                )
                print("Expected prediction:", expected_prediction)

        if status_ok and prediction_ok:
            print("Result: PASS")
            passed += 1
        else:
            print("Result: FAIL")
            print("Expected HTTP status:", expected_status)
            print("Actual HTTP status:", response.status_code)
            failed += 1

    except (requests.RequestException, ValueError) as error:
        print("Result: FAIL")
        print("Error:", error)
        failed += 1


test_prediction(
    "Domestic transaction",
    {"amount": 2000, "international": False},
    200,
    "LOW RISK"
)

test_prediction(
    "International transaction",
    {"amount": 2000, "international": True},
    200,
    "SUSPICIOUS"
)

test_prediction(
    "Negative amount",
    {"amount": -100, "international": False},
    422
)


print("\n===== PREDICTION TEST SUMMARY =====")
print("Total tests:", passed + failed)
print("Passed:", passed)
print("Failed:", failed)

if failed == 0:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED")
