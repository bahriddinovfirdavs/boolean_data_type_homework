def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a>0 and int(a**0.5)==a**0.5
print(main(int(input())))