try:
    num1,num2 = eval(input("Enter two nymbers, seperated by a comma:" ))
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("Comma is missing.Enter numbers seperated by commma like this  1,2")
except:
    print("Wrong input")
else:
    print("No Exceptions")
finally:
    print("THis will execute no matter")