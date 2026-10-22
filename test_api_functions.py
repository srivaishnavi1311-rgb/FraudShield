
import requests

API_URL = "http://127.0.0.1:8000/predict"

passed = 0
failed = 0


def test_api_case(name, data, expected_status):
    global passed, failed

    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=5
        )

        if response.status_code == expected_status:
            print(f"{name}: PASS")
            passed += 1
        else:
            print(f"{name}: FAIL")
            print(f"Expected: {expected_status}")
            print(f"Received: {response.status_code}")
            failed += 1

    except requests.RequestException as error:
        print(f"{name}: FAIL - {error}")
        failed += 1


test_api_case(
    "Valid domestic transaction",
    {"amount": 2000, "international": False},
    200
)

test_api_case(
    "Valid international transaction",
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

test_api_case(
    "Invalid amount text",
    {"amount": "hello", "international": False},
    422
)


print("\n===== TEST SUMMARY =====")
print(f"Total tests: {passed + failed}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")

if failed == 0:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED")
