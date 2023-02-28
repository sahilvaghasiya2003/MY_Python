s = input("Enter any string: ")
print(s)
_list = s.split()  # break the string from space
print(_list)

# multiple string
l = []
for a in range(1, 4):
    n = input("Enter string "+str(a)+":")
    l.append(n)

print(l)
