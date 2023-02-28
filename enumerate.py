list1 = [12, 343, 65.55, "sahil", True]

#print list with index method 1:
rank=0
for item in list1:
    print(rank, item)
    rank += 1
print("---------------------------------")
#print list with index uisng enumerate method 2:

for index, item in enumerate(list1):
    print(index, item)
    index += 1