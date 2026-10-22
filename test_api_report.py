
import requests

API_URL = "http://127.0.0.1:8000/predict"

passed = 0
failed = 0


def test_api_case(name, data, expected_status):
    global passed, failed

    print(f"\nTesting: {name}")

    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=5
        )

        print("HTTP Status:", response.status_code)

        try:
            result = response.json()
        except ValueError:
            result = {}

        if response.status_code == 200:
            print("Prediction:", result.get("prediction"))

        if response.status_code == expected_status:
            print("Result: PASS")
            passed += 1
        else:
            print("Result: FAIL")
            print("Expected status:", expected_status)
            print("Received status:", response.status_code)
            print("Response:", result)
            failed += 1

    except requests.RequestException as error:
        print("Result: FAIL")
        print("Error:", error)
        failed += 1


test_api_case(
    "Domestic transaction",
    {"amount": 2000, "international": False},
    200
)

test_api_case(
    "International transaction",
    {"amount": 2000, "international": True},
    200
)

test_api_case(
    "Negative amount",
    {"amount": -100, "international": False},
    422
)

test_api_case(
    "Missing amount",
    {"international": False},
    422
)


print("\n===== DETAILED TEST REPORT =====")
print("Total tests:", passed + failed)
print("Passed:", passed)
print("Failed:", failed)

if failed == 0:
    print("Overall result: ALL TESTS PASSED")
else:
    print("Overall result: SOME TESTS FAILED")
