users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True] #You can have differnt data types in the same list

emptylist = []

users.append('Elsa')

users.extend(['Robert', 'Jimmy'])

print(users)

#del data # this will delete the assignment to data

data.clear()
print(data)

nums = [4, 42, 78, 1, 5]

nums.reverse()
print(nums)

print(sorted(nums, reverse=True)) #This will reverse the list but won't alter the orginal list assigned to nums

#These are the ways you can create copies of the list 
numscopy = nums.copy()
mynums = list(nums)

mycopy = nums[:]

# Tuples cannot be changed unlike lists

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8)

print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)

newlist.append('Neil')

newtuple = tuple(newlist)

print(newtuple)

# unpacking a tuple assigning values to a tuple

(one, two, *hey) =  anothertuple

print(one)
print(two)
print(hey) #The * holds the remaining values