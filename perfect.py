def is_perfect_number(number):
    """
    Function to check whether a number is a perfect number.

    Parameters:
    - number: The input number to be checked.

    Returns:
    - True if the number is a perfect number, False otherwise.
    """
    if number <= 0:
        return False
    
    # Find divisors and calculate the sum
    divisors_sum = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    # Check if the sum of divisors is equal to the original number
    return divisors_sum == number

# Example usage:
user_number = int(input("Enter a number: "))
result = is_perfect_number(user_number)

if result:
    print(user_number, "is a perfect number.")
else:
    print(user_number, "is not a perfect number.")
