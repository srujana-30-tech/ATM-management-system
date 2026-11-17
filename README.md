# 🏧 ATM Management System

## 📌 Description

The **ATM Management System** is a simple Python-based project that simulates the basic functionalities of an Automated Teller Machine (ATM).

The project is developed using **Object-Oriented Programming (OOP)** concepts. It allows users to securely log in using a PIN and perform common banking operations such as withdrawing money, depositing money, checking account balance, and viewing transaction history.

The application runs through a **Command Line Interface (CLI)** with a menu-driven approach, making it easy for users to interact with the system.

## ✨ Features

- PIN-based login authentication
- Withdraw money from the account
- Deposit money into the account
- Check available account balance
- View mini statement and transaction history
- Exit the ATM system
- Displays success and error messages
- Prevents withdrawals when sufficient balance is unavailable

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP)
- **Interface:** Command Line Interface (CLI)

## 🧠 OOP Concepts Used

### 1. Class
The program uses an `ATM` class to represent the ATM system and group related functionalities together.

### 2. Constructor
The `__init__()` method initializes the ATM's PIN, account balance, and transaction statement when an object is created.

### 3. Encapsulation
The program uses private attributes:

- `__pin`
- `__balance`
- `__statement`

The double underscore (`__`) provides name mangling and helps restrict direct access to these attributes from outside the class.

### 4. Methods
Different ATM operations are implemented using separate methods:

| Method | Description |
|---|---|
| `login()` | Verifies the user's PIN |
| `withdraw()` | Withdraws money from the account |
| `deposit()` | Deposits money into the account |
| `balance_enquiry()` | Displays the available balance |
| `mini_statement()` | Displays transaction history |

## 💳 Initial Values

The ATM system starts with the following default values:

| Attribute | Initial Value |
|---|---|
| PIN | `1234` |
| Initial Balance | ₹10,000 |

**Note:** The PIN is hard-coded for demonstration purposes. This implementation is intended only for learning and should not be used in a real banking application.

## ⚙️ How the Program Works

### Step 1: Login

- The user is asked to enter the ATM PIN.
- If the entered PIN is correct, the system displays `Login Successful`.
- If the PIN is incorrect, the system displays `Wrong PIN`.
- The ATM menu is accessible only after successful authentication.

### Step 2: ATM Menu

After successful login, the following menu is displayed:

1. Withdraw
2. Deposit
3. Balance Enquiry
4. Mini Statement
5. Exit

The user can select an operation by entering the corresponding number.

## 🔄 ATM Operations

### 1. Withdraw Money

- The user enters the amount to withdraw.
- The system checks whether sufficient balance is available.
- If sufficient balance exists, the amount is deducted.
- The transaction is recorded in the mini statement.

**Example:**
```text
Enter amount to withdraw: 2000
Withdrawal Successful
```

If sufficient balance is unavailable:

```text
Insufficient Balance
```

### 2. Deposit Money

- The user enters the amount to deposit.
- The amount is added to the current account balance.
- The transaction is recorded in the mini statement.

**Example:**
```text
Enter amount to deposit: 5000
Deposit Successful
```

### 3. Balance Enquiry

Displays the current available account balance.

**Example:**
```text
Available Balance: 13000
```

### 4. Mini Statement

Displays the transaction history, including deposits and withdrawals.

**Example:**
```text
Mini Statement

Withdraw: 2000
Deposit: 5000
Withdraw: 1000
```

### 5. Exit

Selecting option `5` terminates the ATM program.

**Output:**
```text
Thank You!
```

## 🔀 Program Flow

```text
          START
            |
     Create ATM Object
            |
        Enter PIN
            |
       Verify PIN
            |
      Login Successful?
         /       \
       No         Yes
       |           |
   Wrong PIN   Display Menu
                   |
             Select Operation
                   |
       +-----------+-----------+
       |           |           |
    Withdraw    Deposit    Balance Enquiry
       |           |           |
       +-----------+-----------+
                   |
             Mini Statement
                   |
                 Exit
                   |
                  END
```

## 💻 Example Output

```text
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
```

## 📂 Project Structure

```text
ATM-Management-System/
│
├── ATM.py
│
└── README.md
```

## 🚀 How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installed Python version:

```bash
python --version
```

### Step 2: Clone the Repository

Clone the project repository from GitHub:

```bash
git clone <repository-url>
```

### Step 3: Navigate to the Project Folder

```bash
cd ATM-Management-System
```

### Step 4: Run the Program

Execute the following command:

```bash
python ATM.py
```

### Step 5: Login to the ATM

Enter the default PIN:

```text
1234
```

You can now access the ATM operations through the menu.

## ⚠️ Limitations

This project is developed for educational and demonstration purposes.

- The PIN is hard-coded in the program.
- The account balance is stored only while the program is running.
- No database is used for storing account information.
- No real banking or payment integration is available.
- Only one ATM account is simulated.
- Transaction history is not permanently stored.
- Input validation for negative or invalid transaction amounts may be limited.

## 🔮 Future Enhancements

The project can be further improved by implementing:

- Multiple user accounts
- Secure PIN storage
- PIN change functionality
- Maximum PIN login attempts
- Database integration
- Account number support
- Money transfer functionality
- Transaction date and time
- Improved input validation
- Permanent transaction history
- Receipt generation
- Graphical User Interface (GUI)

## 🎯 Learning Outcomes

Through this project, the following concepts can be understood:

- Python classes and objects
- Constructors and initialization
- Encapsulation and private attributes
- Methods and functions
- Conditional statements
- Loops and iterations
- Lists and data storage
- User input handling
- Menu-driven programming
- Basic transaction management
- Practical implementation of OOP concepts

## 📝 Conclusion

The **ATM Management System** is a beginner-friendly Python project that demonstrates how Object-Oriented Programming can be used to develop a simple banking application.

It provides practical experience with classes, objects, encapsulation, constructors, and methods while simulating essential ATM operations. This project helps strengthen Python programming fundamentals and provides a foundation for developing more advanced banking management applications.
