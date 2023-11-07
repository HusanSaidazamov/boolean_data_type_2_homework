def tekshirish(L, R):
    """
    Check that given L is the length of a circle of radius R.
    Args:
        L: float
        R: float
    Returns:
        bool
    """
    # Write your code here

    uzunlik = 2 * math.pi * R
    if uzunlik == L:
        return True
    else:
        return False
print(main(12))    