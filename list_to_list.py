def remove_duplicates(input_list):
    """
    Function to remove duplicates from a list.

    Parameters:
    - input_list: The input list with possible duplicate elements.

    Returns:
    - A new list with distinct elements from the input list.
    """
    distinct_list = []
    for item in input_list:
        if item not in distinct_list:
            distinct_list.append(item)
    return distinct_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result_list = remove_duplicates(original_list)
print("Original List:", original_list)
print("List with Distinct Elements:", result_list)