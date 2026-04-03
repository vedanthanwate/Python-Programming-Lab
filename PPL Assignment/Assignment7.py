# 1. CALC
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

def mod(a, b):
    return a % b


while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 6:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
    elif choice == 4:
        print("Result:", div(a, b))
    elif choice == 5:
        print("Result:", mod(a, b))
    else:
        print("Invalid choice")


# 2 Bank Account
        balance = 1000  # initial balance


        def display():
            print("Current Balance:", balance)


        def deposit(amount):
            global balance
            balance += amount
            print("Amount Deposited")


        def withdraw(amount):
            global balance
            if amount > balance:
                print("Insufficient Balance")
            else:
                balance -= amount
                print("Amount Withdrawn")


        while True:
            print("\n--- BANK MENU ---")
            print("1. Display Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 4:
                break

            if choice == 1:
                display()
            elif choice == 2:
                amt = int(input("Enter amount: "))
                deposit(amt)
            elif choice == 3:
                amt = int(input("Enter amount: "))
                withdraw(amt)
            else:
                print("Invalid choice")