lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#             0        1       2       3       4
print(friends)
print(friends[0])
print(friends[1:])
print(friends[1:3])
# Adds a list to a list.
friends.extend(lucky_numbers)
print(friends)
# Adds a specific phrase to a list.
friends.append("Creed")
print(friends)
# Adds a specific phrase at a certain place.
friends.insert(1, "Kelly")
print(friends)
# Removes a item from the list.
friends.remove("Jim")
print(friends)
# Completely removes everything.
# friends.clear()
# print(friends)
# Sorts numbers ascending.
lucky_numbers.sort()
print(lucky_numbers)
# Makes a copy of a list.
friends2 = friends.copy()
print(friends2)
