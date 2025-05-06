info = {
    "name": "harry porter",
    "description": "A dictionary set of Harry Porter",
    "charatcers": [
        "Harry Potter",
        "Hermione Granger",
        "Ron Weasley",
    ]
}
info["full_name"] = "Harry Porter and the Philosopher's Stone"

print(info.keys())
print(info.values())
print(info.items())

print(info.get("name"))
print(info.get("no_name", "not found"))

#######################################
### Set

collection_set = {1, 2, 3, 4, 5}

print(type(collection_set))
print(collection_set)

# Add element
collection_set.add(6)
print(collection_set)

# Remove element
collection_set.remove(6)
print(collection_set)

# Clear set
collection_set.clear()
print(collection_set)

# collection_set.add({1, 2}) - Error we cant add
print(collection_set)

print(len(collection_set))

# Ser operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  # Union -- Returns new set with all unique elements
print(set1.intersection(set2))  # Intersection -- Returns new set with common elements

