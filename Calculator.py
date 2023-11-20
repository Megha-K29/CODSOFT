

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2==0:
        return "Cannot divide by ZERO"
    return num1/num2

while True:
    print("1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Exit\n")

    choice=int(input("Enter choice (1/2/3/4/5): "))

    if (choice==5):
        print("Exiting")
        break

    num1=float(input("Enter First Number: "))
    num2=float(input("Enter Second Number: "))

    if (choice==1):
        print(num1, "+" ,num2, "=", add(num1,num2))
    elif (choice==2):
        print(num1, "-", num2, "=", sub(num1,num2))
    elif (choice==3):
        print(num1, "*", num2, "=", multiply(num1,num2))
    elif (choice==4):
        print(num1, "/", num2, "=", divide(num1,num2))
    else:
        print("Invalid Choice")


