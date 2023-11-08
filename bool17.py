def main(L, R):
    pi=3.141592653589793
    """
    Check that given L is the length of a circle of radius R.
    Args:
        L: float
        R: float
    Returns:
        bool
    """
    # Write your code here

    uzunlik = 2 * pi * R
    if uzunlik == L:
        return True
    return False
print(main(12))    