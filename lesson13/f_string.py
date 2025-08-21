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