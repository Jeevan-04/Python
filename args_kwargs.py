# Write a program to take input as name, email & age   from user using combination of keywords argument and positional arguments (*args and**kwargs) using function
def get_user_details(*args, **kwargs):
    """
    Function to get user details.

    Parameters:
    - *args: Positional arguments (name, email, age)
    - **kwargs: Keyword arguments

    Returns:
    - Dictionary containing user details
    """
    user_details = {}

    # Check if positional arguments are provided
    if len(args) >= 3:
        user_details['name'] = args[0]
        user_details['email'] = args[1]
        user_details['age'] = args[2]

    # Update with keyword arguments
    user_details.update(kwargs)

    return user_details

# Example usage:
name_input = input("Enter your name: ")
email_input = input("Enter your email: ")
age_input = int(input("Enter your age: "))

# Using the function with a combination of positional and keyword arguments
user_info = get_user_details(name_input, email_input, age_input, city='Example City', country='Example Country')

# Display the user details
print("\nUser Details:")
for key, value in user_info.items():
    print(f"{key}: {value}")