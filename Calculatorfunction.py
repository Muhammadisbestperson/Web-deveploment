def get_numbers():
    n1=float(input("Enter Number one"))
    n2=float(input("Enter Second number"))
    return (n1,n2)

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def display_result(result):
    print("result",result)
    
user_inputs=get_numbers()
print("user_inputs",user_inputs)
opr=int(input("Type 1 for addition Type 2 for Subtraction Type 3 for Multiplying type 4 for division"))
n1=user_inputs[0]
n2=user_inputs [1]
if opr == 1:
    result=add(n1,n2)
elif opr==2:
    result=subtract(n1,n2)
elif opr==3:
    result=multiply(n1,n2)
elif opr==4:
    result=divide(n1,n2)

display_result(result)