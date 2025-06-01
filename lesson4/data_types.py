# String data type

# Literal assignment
first = "Dave"
last = "Gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Changing a number to a string 

decade = str(1980)
print(type(decade))
print(decade)


# Multi line

multiline = '''
Hey, how are you?

I was just checking in.

                    All good

'''

print(multiline)

#Escaping special characters 

#all you need is the \ to escape the special character in this case it's \
sentence = 'I\'m'

print(sentence)

# \t is used to tab. \n i used to create a new line and \\ is used to show 
# The \ but due to it been used as an escape character you need to put it twice 

sentence = 'I\'m back at work! \t Hey! \n\n this is at \\located?'

print(sentence)

print(multiline.replace("good", "ok"))

# Build a menu

print(" ")
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(20, ".") + "$1".rjust(4))
print("Muffin".ljust(20, ".") + "$2".rjust(4))
print("Cheesecake".ljust(20, ".") + "$4".rjust(4))

# string index values

print("")

test = "Bingo"

print(test[1])

#This allows you to get the last value in the word;
print(test[-1])

print(test[1:-1])
print(test[1:])


# Some methods return boolean data 

print(test.startswith("B"))
print(test.endswith("Z"))

#Boolean data type
print(" ")

myvalue = True

x = bool(False)

print(type(myvalue))
print(isinstance(myvalue, bool))


