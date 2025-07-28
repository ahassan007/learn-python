
# You can pass a function to itself so it runs indefinitely
def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total)

# To inculde number 10 we need to capture the result og add_one(0) and print it
new_add_one = add_one(0)

print(new_add_one)