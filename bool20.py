def main(a):
    """
    Given integer is less of 10000 . Check if the sum of digits is odd .
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a < 10000 and sum(int(digit) for digit in str(a)) % 2 != 0
print(main(1000))