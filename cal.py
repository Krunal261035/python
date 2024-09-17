def add(a,b):
    return  a+b

def subtr(a,b):
    return a-b

def div(a,b):
    if a==0:
        print("divide is not possible")

    else:
        return a/b
    
def multi(a,b):
    return a*b

print("1. addition")
print("2. subtraction")
print("3. division")
print("4. multiplication")
# print("1. addition")

choice = int(input("Enter the operation:"))

print(f"you had selected {choice} operation")

num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))

match choice:
    case 1:
        print(add(num1,num2))
    
    case 2:
        print(subtr(num1,num2))

    case 3:
        print(div(num1,num2))

    case 4:
        print(multi(num1,num2))


    case _:
        print("please selcet the proper operation")
        