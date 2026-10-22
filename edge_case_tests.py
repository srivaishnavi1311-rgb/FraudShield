# FraudShield - Edge Case Testing

def check_transaction(amount, international):
    if amount < 0:
        return "INVALID AMOUNT"

    if amount == 0:
        return "ZERO AMOUNT"

    if amount >= 50000 or international:
        return "SUSPICIOUS"

    return "LOW RISK"


# Test cases
test_cases = [
    (0, False),
    (-100, False),
    (1000000, False),
    (2000, True)
]

for amount, international in test_cases:
    result = check_transaction(amount, international)

    print(
        f"Amount: ₹{amount:,.2f} | "
        f"International: {international} | "
        f"Result: {result}"
    )