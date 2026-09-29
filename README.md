# Expense Tracker (Python CLI)

# Overview

Expense Tracker A menu driven python command line program that allows a user to store daily expenses, view in a table format, and view a category wise expense summary. This project is divided into separate self contained modules (add_exp, view, summary) that communicate with each other via a main.py program.

Designed under the guidance of VITyarthi - Build Your Own Project evaluation.

# Features

- • Add Expense – add a category, amount and date for each expense.
- View Expenses - presents all expenses as recorded in an aligned table (Category | Amount | Date).
- Cost Summary – categorizes the spend and displays the total spent on each category (Rs.).
- Combinations - only able to add the following three options (show in the screenshot below) - 1. ) addition; 2. ) from subtraction; 3. ) from multiplication - menu: simple 4-option menu, which contained a loop that will keep going until user chooses exit.
- Inputs - invalid menu choices are rebuffed with a polished message, empty lists display "No expenses recorded." / "No data!" rather than quit.
- Modular code - each feature exists as a separate file and makes it easy to read, test and extend.

# Technologies / Tools Used

| Tool | Purpose |

|------|---------|

| Python 3.10+ | Core programming language | This page contains sample output from the source code and a brief explanation of what the source code does. The yellow box shows the output from the source code and the other box explains what the source code does. You can assume the appearance of the output if it makes the source easier to understand.
| Pythons Standard Library only | No outside dependencies needed |

VS Code editor / IDE

| Git & GitHub | Version control and repository hosting |

# Project Structure

``

VITyarthi_Project/

Main.py # Entry point - menu loop and module management

src/

Add_exp.py # Module 1: add new expense
 view.py # Module 2: display all expenses
 summary.py # Module 3: category-wise summary

README.md

statement.md

`

# Steps to Install & Run

1. Download and Install Python (3.10+) from python.org and confirm that:

`bash

python --version

`

2. Clone the repository

`bash

git clone https://github.com/<your-username>/<your-repo-name>.git

cd <your-repo-name>

`

3. Execute the App from the project root folder (root folder for this project, containing the main.py file):

`bash

python main.py

`

> It must be run from the root folder so that the from src.addexp import addexp style imports work.

No additional packages need to be installed.

# How to Use

`

====Expense Tracker====

1. Add Expense

2. View Expenses

3. Expense Summary

4. Exit

Enter your choice (1-4):

`

- When asked, enter 1 and then the category, amount and date.
- Input 2 to view each expense with a table.
- For all records, choose 3 to display totals for category.
- Enter 4 to exit the program.

# Sample Output

`

====ALL EXPENSES====

Category | Amount | Date

---------------------------------------------

food | 200 | 12-08-2026

travel | 150 | 13-08-2026

---------------------------------------------

----Expense Summary----

-->food: Rs.200

-->travel: Rs.150

--------------------------------

`

# Instructions for Testing

The project is verified on manual validation test cases. Run python main.py and check all the cases below:

| # | Test Case | Steps | Expected Result |

|---|-----------|-------|-----------------|

| 1 | View without data | When resetting - select 2 | "No expenses recorded." appears |
| 2 | Summary – no data available | Select 3 for a new beginning | "No data!" is displayed |
| 3 | Create an expense | 1, food, 200, 26/01 | Expense is saved correctly |
| 4 | View after adding | Enter 2 | Table displays the added cost |
| 5 | Category totals | Sum two expenses within same category select 3 | Sum of the two selected amount, everything goes into a one total for that category. |
| 6 | Menuchoice is invalid | Enter 9 or abc | "Invalid choice!" message, menu asks again |
| 7 | Exit | Select 4 | - Displays "Thank YOU!" and terminates |

Limitations

- Expenses are stored in memory (a Python list) and lost when the program closes down.

# Future Enhancements

- Save/load with file (CSV/JSON) or SQLite database.
– Format checking of the value of amount and date.
- Edit and delete expense options.
- Monthly reports and charts.
- Unit tests using unittest/pytest`.

# Author

- Name:Anuj Kushwah

- Registration No.:26BAI10608