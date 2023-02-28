while (True):

    try:
        a = int(input("Enter a number: "))
        b = 100 / a
        print(b)
    except ValueError as e:
        print("Please enter a valid number..")
    except ZeroDivisionError as e:
        print("Make sure you are not dividedby zero...")
    except Exception as e:
        print({e})
print("than you")
