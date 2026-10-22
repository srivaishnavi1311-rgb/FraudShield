
def expected_risk(amount, international):
    if amount > 50000 or international == "yes":
        return "SUSPICIOUS"
    return "LOW RISK"


test_amounts = [49999, 50000, 50001]

print("===== Intended Rule Check =====")

for amount in test_amounts:
    result = expected_risk(amount, "no")
    print("Amount:", amount, "| Expected:", result)
