# FraudShield - Input Validation

def validate_transaction(amount, international):

    # Check if amount is missing
    if amount is None:
        return "ERROR: Amount is required"

    # Check whether amount is a number
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return "ERROR: Amount must be a number"

    # Check for negative amounts
    if amount < 0:
        return "ERROR: Amount cannot be negative"

    # Check for a valid international value
    if not isinstance(international, bool):
        return "ERROR: International must be True or False"

    return "Input is valid"


# Test cases
test_cases = [
    (2000, False),
    (None, False),
    ("hello", False),
    (-100, False),
    (2000, "yes"),
]

for amount, international in test_cases:
    result = validate_transaction(amount, international)
    print(
        f"Amount: {amount!r} | "
        f"International: {international!r} | "
        f"Result: {result}"
    )