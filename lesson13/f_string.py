person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins) # older way of doing things

print(message)

message = "\n{} has {} coins left.".format(person, coins) # Another way of doing it

print(message)

message = "\n{1} has {0} coins left.".format(coins, person) # Another way of doing it

print(message)

message = "\n{person} has {coins} coins left.".format(person=person,coins=coins) # Another way of doing it

print(message)

player = {'person': 'Dave', 'coins':3}

message = "\n{person} has {coins} coins left.".format(**player) # Another way of doing it

print(message)

#######
# f-strings! This is the way

message = f"\n{person} has {coins} coins left" # Just use the letter f 
print(message)

message = f"\n{person} has {2 * 5 } coins left" # Just use the letter f 
print(message)

message = f"\n{person.lower()} has {2 * 5 } coins left" # Just use the letter f 
print(message)

message = f"\n{person.lower()} has {2 * 5 } coins left" # Just use the letter f 
print(message)

message = f"\n{player['person']} has {2 * 5 } coins left" # Just use the letter f 
print(message)


#######
# You can pass formatting options

num = 10
print(f"\n2.5 times {num} is {2.5 * num:.2f}\n") # This will fromat the value of num to two decemal places f stands for fixed



for num in range(1,11):
    print(f"2.5 times {num} is {2.5 * num:.2f}") 


for num in range(1,11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}") 