# ATM Management System

## Description

This project is a simple ATM Management System developed using Python. It demonstrates basic Object-Oriented Programming (OOP) concepts by simulating common ATM operations such as PIN login, withdrawal, deposit, balance enquiry, and mini statement.

The program runs in the command line and allows the user to interact with the ATM through a menu-driven interface.

## Features

* PIN-based login
* Withdraw money
* Deposit money
* Check available balance
* View mini statement
* Exit the ATM system
* Displays messages for successful and unsuccessful operations
* Prevents withdrawal when the available balance is insufficient

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Command Line Interface (CLI)

## OOP Concepts Used

### 1. Class

The program uses an `ATM` class to represent the ATM system.

### 2. Constructor

The `__init__()` method initializes the ATM's PIN, balance, and transaction statement.

### 3. Encapsulation

The variables `__pin`, `__balance`, and `__statement` are private attributes. The double underscore `__` provides name mangling and helps restrict direct access to these attributes from outside the class.

### 4. Methods

Different ATM operations are implemented using methods:

* `login()` – Handles PIN verification
* `withdraw()` – Handles money withdrawal
* `deposit()` – Handles money deposit
* `balance_enquiry()` – Displays available balance
* `mini_statement()` – Displays transaction history

## Initial Values

The ATM starts with:

* PIN: `1234`
* Initial Balance: `10000`

Note: The PIN is hard-coded for demonstration purposes and should not be used this way in a real banking application.

## How the Program Works

### Step 1: Login

The user is asked to enter the ATM PIN.

If the entered PIN is correct, the program displays:

`Login Successful`

If the PIN is incorrect, the program displays:

`Wrong PIN`

The ATM menu is displayed only after successful login.

### Step 2: ATM Menu

After successful login, the following menu is displayed:

1. Withdraw
2. Deposit
3. Balance Enquiry
4. Mini Statement
5. Exit

The user can select an operation by entering the corresponding number.

## Operations

### 1. Withdraw

The user enters the amount they want to withdraw.

If sufficient balance is available, the amount is deducted from the account and the transaction is added to the mini statement.

Example:

`Enter amount to withdraw: 2000`

`Withdrawal Successful`

If the balance is insufficient, the program displays:

`Insufficient Balance`

### 2. Deposit

The user can deposit money into the account.

Example:

`Enter amount to deposit: 5000`

`Deposit Successful`

The deposited amount is added to the current balance and recorded in the statement.

### 3. Balance Enquiry

This option displays the current available balance.

Example:

`Available Balance: 13000`

### 4. Mini Statement

This option displays the transaction history of withdrawals and deposits.

Example:

`Mini Statement`

`Withdraw: 2000`

`Deposit: 5000`

`Withdraw: 1000`

### 5. Exit

Selecting option `5` exits the ATM program.

The program displays:

`Thank You!`

## Program Flow

Start → Create ATM Object → Enter PIN → Verify PIN → Display ATM Menu → Select Operation → Withdraw / Deposit / Balance Enquiry / Mini Statement / Exit → End

## Example Output

Enter PIN: 1234

Login Successful

1. Withdraw
2. Deposit
3. Balance Enquiry
4. Mini Statement
5. Exit

Enter your choice: 1

Enter amount to withdraw: 2000

Withdrawal Successful

1. Withdraw
2. Deposit
3. Balance Enquiry
4. Mini Statement
5. Exit

Enter your choice: 3

Available Balance: 8000

1. Withdraw
2. Deposit
3. Balance Enquiry
4. Mini Statement
5. Exit

Enter your choice: 4

Mini Statement

Withdraw: 2000

1. Withdraw
2. Deposit
3. Balance Enquiry
4. Mini Statement
5. Exit

Enter your choice: 5

Thank You!

## Project Structure

ATM-Management-System/
│
├── ATM.py
└── README.md

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version using:

`python --version`

### 2. Clone the Repository

If the project is hosted on GitHub:

`git clone <repository-url>`

### 3. Open the Project Folder

`cd ATM-Management-System`

### 4. Run the Program

`python ATM.py`

### 5. Enter the PIN

Use the default PIN:

`1234`

## Limitations

This project is created for learning and demonstration purposes.

* The PIN is hard-coded.
* The account balance is stored only while the program is running.
* No database is used.
* There is no real banking or payment integration.
* Negative or invalid transaction amounts are not specifically validated.
* Only one ATM account is simulated.
* Transaction history is not permanently stored.

## Future Enhancements

The project can be improved by adding:

* Multiple user accounts
* Secure PIN storage
* PIN change functionality
* PIN attempt limit
* Database integration
* Account number support
* Money transfer functionality
* Transaction date and time
* Better input validation
* Permanent transaction history
* Receipt generation
* Graphical User Interface (GUI)

## Learning Outcomes

Through this project, the following concepts can be understood:

* Python classes and objects
* Constructors
* Encapsulation
* Private attributes
* Methods
* Conditional statements
* Loops
* Lists
* User input
* Menu-driven programming
* Basic transaction management

## Conclusion

The ATM Management System is a beginner-friendly Python project that demonstrates how Object-Oriented Programming can be used to build a simple real-world application. It provides basic ATM functionality such as authentication, withdrawal, deposit, balance enquiry, and transaction history through a command-line interface.

## Author

Developed as a Python/OOP academic project.
