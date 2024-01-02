# Given list
original_list = [1, 2, 3]

# i. By using + operator
extended_list_1 = original_list + [4, 5, 6]

# ii. By using Append()
original_list.append([7, 8, 9])
extended_list_2 = original_list

# iii. By using extend()
original_list = [1, 2, 3]  # Resetting original list
original_list.extend([4, 5, 6])

# Displaying the results
print("Original List:", original_list)
print("Extended List (using + operator):", extended_list_1)
print("Extended List (using append()):", extended_list_2)
print("Extended List (using extend()):", original_list)
