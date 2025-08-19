name = "Dave" # This is a global scope meaning it's anyone can use it

def greeting():
    color = "blue"
    print(color)
    print(name)

# print(color) <= This will not work as color is defined on the local level for greeting

count = 1

def another():
    global count # To use a global var locally you need to define it using the global key word
    count += 1
    print(count)


another()