def add(x, y):
    return x+y
def substract(x, y):
    return x-y
def multiplication(x, y):
    return x*y
def divide(x, y):
    return x/y


print("select opetation.")
print("1.add")
print("2.substract")
print("3.multiplicatio")
print("4.divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number"))

if choice == '1':
    print( num1, "+", num2,"=", add(num1,num2))
elif choice == '2':
    print(num1, "-", num2,"=", substract(num1,num2))
elif choice == '3':
    print(num1, "*", num2,"=", multiplication(num1,num2))
elif choice == '4':
    print(num1, "/", num2,"=", divide(num1,num2))
else:
    print("Invalid input")









