def calculator():
    print("Simple calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Operations")
    print("1. Addition +56 ")
    print("2. Subtraction - ")
    print("3. Multiplication * ")
    print("4. Division / ")
    operation = input("choose operation(1-4): ")
    if operation =='1':
         result = num1+num2
         print(f"{num1}+{num2}= {result}")
    elif operation == '2':
        result=num1-num2
        print(f"{num1}-{num2}={result}")
    elif operation=='3':
         result=num1*num2
         print(f"{num1}*{num2} = {result}")
    elif operation == '4':
         if num2 !=0:
             result=num1/num2
             print(f"{num1}/{num2}={result}")
         else:
             print("Error:Division by Zero")
    else:
         print("Invalid operation. Please choose a number between 1 & 4.")
if __name__=="__main__":
    calculator()
45
65