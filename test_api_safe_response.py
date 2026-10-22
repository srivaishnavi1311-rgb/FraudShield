
import requests

API_URL = "http://127.0.0.1:8000/predict"

passed = 0
failed = 0


def test_api_case(name, data, expected_status,
                  expected_prediction=None):
    global passed, failed

    print(f"\nTesting: {name}")

    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=5
        )

        print("HTTP Status:", response.status_code)

        # Safely read the JSON response
        try:
            result = response.json()
        except ValueError:
            result = None

        # Check that the response is a dictionary
        if not isinstance(result, dict):
            print("Result: FAIL - Invalid response format")
            failed += 1
            return

        # Check the expected HTTP status
        if response.status_code != expected_status:
            print("Result: FAIL - Unexpected status code")
            print("Expected:", expected_status)
            print("Received:", response.status_code)
            failed += 1
            return

        # Check the prediction when one is expected
        if expected_prediction is not None:
            actual_prediction = result.get("prediction")
            print("Actual prediction:", actual_prediction)

            if actual_prediction != expected_prediction:
                print("Result: FAIL - Unexpected prediction")
                failed += 1
                return

        print("Result: PASS")
        passed += 1

    except requests.RequestException as error:
        print("Result: FAIL - Request error")
        print(error)
        failed += 1


test_api_case(
    "Domestic transaction",
    {"amount": 2000, "international": False},
    200,
    "LOW RISK"
)

test_api_case(
    "International transaction",
    {"amount": 2000, "international": True},
    200,
    "SUSPICIOUS"
)

test_api_case(
    "Negative amount",
    {"amount": -100, "international": False},
    422
)


print("\n===== SAFE API TEST SUMMARY =====")
print("Total tests:", passed + failed)
print("Passed:", passed)
print("Failed:", failed)

if failed == 0:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED")
