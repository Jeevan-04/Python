def count_upper_lower(string):
    """
    Function to count the number of upper- and lower-case letters in a given string.

    Parameters:
    - string: The input string.

    Returns:
    - Tuple containing the count of upper-case letters and lower-case letters.
    """
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
string_test = 'Today is My Best Day'
result = count_upper_lower(string_test)

print("Count of upper-case letters:", result[0])
print("Count of lower-case letters:", result[1])
