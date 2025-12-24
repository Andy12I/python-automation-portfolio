friends = ["Rahul", "Sweety", "Amrit", "Pooja"]

print("Original lists:", friends)

friends.append("Pankaj")
friends.remove("Sweety")

friends[1] = "Shivani"

print("after changing Amrit to Shivani:", friends)
friends.sort()
print("sorted list:", friends)
print("Number of friends:", len(friends))
print("\nHere is the list one-by-one:")
for name in friends:
    print("_", name)