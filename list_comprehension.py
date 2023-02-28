a = [13, 23, 33, 53, 44, 65, 6]
# #method 1
# b=[]

# for i in a:
#     if i%2 == 0:
#         b.append(i)
# print(b)

b = [i for i in a if i%2 == 0]
print(b)