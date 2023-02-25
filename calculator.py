val1 = input("Enter first value: ")
val2 = input("Enter second value: ")
operator = input("Enter operator (+ , - , * , /): ")

val1 = int(val1)
val2 = int(val2)

if operator == '+':
    print(val1+val2)
elif operator == '-':
    print(val1-val2)
elif operator == '*':
    print(val1*val2)
elif operator == '/':
    print(val1/val2)
elif operator == '%':
    print(val1 % val2)
else:
    print("enter valid operator...")
