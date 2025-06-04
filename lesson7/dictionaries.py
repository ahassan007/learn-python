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

band2 = band # create a reference any changes made to either band2 or band will affect both as they share the same memeory space

print("Bad copy!")
print(band2)
print(band)

band2["drums"] = "Dave"

print(band)