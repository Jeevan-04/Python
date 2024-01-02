# Function to create a dictionary of cubes of odd numbers in a given range
def create_odd_cubes_dictionary(start, end):
    odd_cubes_dict = {}

    for num in range(start, end + 1):
        if num % 2 != 0:  # Check if the number is odd
            odd_cubes_dict[num] = num ** 3  # Cube of the odd number

    return odd_cubes_dict

# Input: User enters the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Create the dictionary of cubes of odd numbers in the given range
result_dict = create_odd_cubes_dictionary(start_range, end_range)

# Display the result
print("Dictionary of cubes of odd numbers:", result_dict)
