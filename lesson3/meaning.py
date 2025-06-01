meaning = 20
print('')

# if meaning > 10:
#     print('Right on!')
# else:
#     print('Not Today!')

# Ternary operator

print('Right On!') if meaning > 10 else print('Not today!')


# Not inverts the boolean value of an expression if it's true it changes it to false 

# Example 1: Basic usage
print(not True)    # Output: False
print(not False)   # Output: True

# not x>5 if x is 4 it will return true as 4 is less than 5 but due to the not it changes it to true
# Example 2: With comparisons
x = 10
print(not (x > 5))  # x > 5 is True → not True → False

# Example 3: In a condition
if not (5 == 10):
    print("5 is not equal to 10")  # This will print
