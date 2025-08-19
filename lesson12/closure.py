# closure is a function having access to the scope of its parent 
# function after the parent function has returned


def parent_function(person, coins):
    # coins = 3 # this will be our global var

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")
    
    return play_game


tommy = parent_function("Tommy", 2)
Jen = parent_function("Jen", 5)

Jen() # This will print Jen has 4 coins
tommy() # This iwll print tommy has 1 coin left
tommy() # This will print tommy is out of coins

# parent_function("Tommy") → returns a function object.
# tommy = parent_function("Tommy") → saves that function with state.
# tommy() → actually runs it, updating its closure variables.
# Without (), you just hold the function reference.
# Each call to the parent function makes a new closure with its own state.


def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


# This section will call multi and assign 2 and 3 to factor but it's still not ran the function inside
double = multiplier(2)
triple = multiplier(3)

# Here you are takking the value double for example which already has a parent factor of 2 and assigning 
# number the value of 5
print(double(5))  # 10
print(triple(5))  # 15
