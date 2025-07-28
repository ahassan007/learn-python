# def sum(num1, num2):
#     print(num1 + num2)

# sum(100,3)

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

print(sum(100,3))
print(sum(9,10))

# print(sum("a", 2)) this returns none

# Functions with defualts only num1 is required num2 has a default value of 3

def sum_default(num1, num2=3):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

print(sum_default(100))
print(sum_default(9))

# When you don't now how many values that will be passed ot a function use this method
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")

# kwargs stands for key word arguments it's used for dict arg that are not defined
def mult_named_itmes(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_itmes(first ="Dave", last ="Gray")