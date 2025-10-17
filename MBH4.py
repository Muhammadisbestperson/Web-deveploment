try:
    number=int(input("ENTER A NUMBER"))
    print("The number entered id", number)
except ValueError as ex:
    print("Exception:",ex)