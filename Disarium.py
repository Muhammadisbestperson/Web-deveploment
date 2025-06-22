def is_disarium(num):
    """
    Checks if a given number is a Disarium number.

    Args:
        num: An integer.

    Returns:
        True if the number is a Disarium number, False otherwise.
    """
    str_num = str(num)  # Convert the number to a string to easily access digits
    disarium_sum = 0
    for i, digit_char in enumerate(str_num):
        # Enumerate provides both index (position) and value (digit)
        # Position starts from 0, so add 1 for the power
        disarium_sum += int(digit_char) ** (i + 1)
    
    return disarium_sum == num

# Example usage:
print(f"Is 175 a Disarium number? {is_disarium(175)}")
print(f"Is 89 a Disarium number? {is_disarium(89)}")
print(f"Is 123 a Disarium number? {is_disarium(123)}")