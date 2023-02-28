def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Please enter only number...")


a = increment(3455)
print(a)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
a = increment('df3455')
print(a)
