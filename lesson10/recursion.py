
# You can pass a function to itself so it runs indefinitely
def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total)

# To inculde number 10 we need to capture the result og add_one(0) and print it
mynewtotal = add_one(10)

print(mynewtotal)

# Use a loop to do the same thing

# def add_one_loop(num):
#     while num <= 9:
#         num += 1
#         print(num)

def add_one_loop(num):
    while num < 9:
        num += 1
        print(num)
    return num + 1

print(add_one_loop(10))



# def factorial(n):
#     if n == 1:              # Base case
#         return 1
#     return n * factorial(n - 1)  # Recursive case
# print(factorial(5))  # Output: 120