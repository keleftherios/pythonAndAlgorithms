def finding_gcd(a, b):
    """
    Implementation of Greatest Common Divider (GCD) algorithm
    """
    while a % b != 0:
        a, b = b, a % b
    return b


if __name__ == "__main__":

    R1 = finding_gcd(21, 12)
    print(R1)
    assert R1 == 3, "Wrong output..."

    R2 = finding_gcd(20, 10)
    print(R2)
    assert R2 == 10, "Wrong output..."




