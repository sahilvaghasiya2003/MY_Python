list_1 = [10,20,30,40]
list_2 = [11,22,33,44]


#using zip() function
for a,b in zip(list_1, list_2):
    print(a,b)

#using simple for loop

t=len(list_1)

for d in range(t):
    print(list_1[d], list_2[d])