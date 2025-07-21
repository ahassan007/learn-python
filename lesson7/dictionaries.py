# Dictionairies 

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

#Access items 
print(band["vocals"])

print(band.get("guitar"))

#List all keys

print(band.keys())

# List all values 

print(band.values())

# Change values

band["vocals"] = "Coverdale"

print(band["vocals"])

band.update({"bass": "JPJ"})

print(band["bass"])

#Remove item

print(band.pop("bass"))

print(band)


#Delete and clear

band["drums"] = "Bonham"

del band["drums"]

print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# How not to create a copy

# band2 = band # create a reference any changes made to either band2 or band will affect both as they share the same memeory space

# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"

# print(band)

# Correct way to copy a dictionary

band2 = band.copy()

band2["drums"] = "Dave"

print("Good copy")
print(band)
print(band2)

#Use the contructor function to make a copy

band3 = dict(band)
print("Good copy")
print(band3)

# Nested Dictionaries 

member1 = {
    "name" : "Plant",
    "instrument" : "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)

print(band["member1"]["name"])

# Sets

nums = {1, 2,3,4}

nums2 = set((1,2,3,4))

print(nums)

# No duplicates allowed 

nums = {1, 2, 2, 3 }
print(nums)

# True is a duplicate of 1, False is a supl of 0

nums = {1, True, 2, False, 3, 4, 0}

print(nums)

#Check if a vlaue is in a set 

print(2 in nums)
# You cannot refer to an elment in the set with an index position or a key 
nums.add(8)

print(nums)

# Add elemnts form one set to another 

morenums = {5, 6, 7}

nums.update(morenums)

print(nums)

# You can use update with lists, tuples, and dictionaries too

one = {1, 2, 3}

two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

#Keep only the duplicates 
one = {1, 2, 3}

two = {2,3,4}

one.intersection_update(two)
print(one)

#Keep everything but the duplicates 
one = {1, 2, 3}

two = {2,3,4}

one.symmetric_difference_update(two)

print(one)