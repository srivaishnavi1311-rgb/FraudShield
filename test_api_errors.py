
import requests

API_URL = "http://127.0.0.1:8000/predict"

test_cases = [
    {
        "name": "Negative amount",
        "data": {"amount": -100, "international": False}
    },
    {
        "name": "Invalid Boolean",
        "data": {"amount": 2000, "international": "yes"}
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

        if response.status_code == 422:
            error_data = response.json()

            if "detail" in error_data:
                print(f'{case["name"]}: PASS')
                print("Error details:", error_data["detail"])
                passed += 1
            else:
                print(f'{case["name"]}: FAIL - Missing error details')
                failed += 1
        else:
            print(
                f'{case["name"]}: FAIL - '
                f'Expected 422, received {response.status_code}'
            )
            failed += 1

    except (requests.RequestException, ValueError) as error:
        print(f'{case["name"]}: FAIL - {error}')
        failed += 1

print("\n===== ERROR TEST SUMMARY =====")
print(f"Total tests: {passed + failed}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
