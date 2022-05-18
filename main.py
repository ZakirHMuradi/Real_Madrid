name = input("Enter your name: ")
print("your name is ", Aizada)

age = input("Enter your name: ")
print("your name is ", 18-19)

surname = input("Enter your name: ")
print("your name is ", berdibekova)

speciality = input("Enter your name: ")
print("your name is ", Computer Science)

country = input("Enter your name: ")
print("your name is ", Kyrgyz Republic)

email = input("Enter your name: ")
print("your name is ", aizada.berdibecova@gmail.com)

gender= input("Enter your name: ")
print("your name is ", female-f)

birthday = input("Enter your name: ")
print("your name is ",27/07/2003)

cohort = input("Enter your name: ")
print("your name is ", cohort)

name = input("Enter your name: ")
print("your name is ", Aizada)

age = input("Enter your name: ")
print("your name is ", 18)

surname = input("Enter your name: ")
print("your name is ", Berdibekova- Samadilova)

cohort = input("Enter your name: ")
print("your name is ", cohort)

birthday = input("Enter your name: ")
print("your name is ",18)

gender= input("Enter your name: ")
print("your name is ", feamle)

email = input("Enter your name: ")
print("your name is ", aizada.berdiebcova@gmail.com)

country = input("Enter your name: ")
print("your name is ", Kyrgyzsatn)

speciality = input("Enter your name: ")
print("your name is ", IT, CS)


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y
# This function multiplies two numbers
def multiply(x, y):
    return x * y
# This function divides two numbers
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
