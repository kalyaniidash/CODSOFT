def addition(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y==0:
        return "ERROR:Division By Zero"
    else:
        x/y

def main():
    print("Calculator")
    print("options:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    while True:
        try:
            choice =int(input("Enter your choice(1/2/3/4/5):"))
            if choice == 5:
                print("Existing the calculator.Good Bye!")
                break
            if choice not in [1,2,3,4]:
                print("Invalid choice.Please try again.")
                continue
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))

            if choice == 1:
                print(f"Result: {num1} + {num2} ={addition(num1,num2)}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} ={substraction(num1,num2)}")
            elif choice == 3:
                print(f"Result: {num1} * {num2} ={substraction(num1,num2)}") 
            elif choice == 4:
                result =division(num1,num2)
                print(f"Result: {num1} / {num2} ={result}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()