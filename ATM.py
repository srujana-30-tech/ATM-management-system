class ATM:
    def __init__(self):
        self.__pin = "1234"      
        self.__balance = 10000
        self.__statement = []

    def login(self):
        pin = input("Enter PIN: ")
        if pin == self.__pin:
            print("Login Successful")
            return True
        else:
            print("Wrong PIN")
            return False

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.__balance:
            self.__balance -= amount
            self.__statement.append(f"Withdraw: {amount}")
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.__balance += amount
        self.__statement.append(f"Deposit: {amount}")
        print("Deposit Successful")

    def balance_enquiry(self):
        print("Available Balance:", self.__balance)

    def mini_statement(self):
        print("\nMini Statement")
        for i in self.__statement:
            print(i)

atm = ATM()
if atm.login():
    while True:
        print("\n1. Withdraw")
        print("2. Deposit")
        print("3. Balance Enquiry")
        print("4. Mini Statement")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            atm.withdraw()
        elif choice == 2:
            atm.deposit()
        elif choice == 3:
            atm.balance_enquiry()
        elif choice == 4:
            atm.mini_statement()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")