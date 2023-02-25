item = [92, 94, 97, 99, "maths"]
# print all list
print(item)

# print list as per index
print(item[2])
print(item[4])
print(item[-4])

# print list as a sub list
print(item[1:4])

# print using for loop

for list in item:
    print(list)

# print using while loop

i = 0
while i < len(item):
    print(item[i])
    i = i+1

# various function of list

item.append(66)
print(item)

item.insert(2, 88)
print(item)

item.remove(97)
print(item)

print(len(item))

item.clear()
print(item)
