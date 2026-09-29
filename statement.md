# Project Statement - Expense Tracker

# Problem Statement

Most students and people forget to trace where their cash has gone. Money is then budgeted in bits and pieces across the remembrances, paper and electronic notes and chats, and no one really knows how much he or she has spent, what and when. Without a simple to write a record and summarize, people overspend on some things, and don't measure budget.

A simple and fast command line Expense Tracker which allows the user to input expenses, display the list of entered expenses in an organized manner and view the category-wise expenditure summary.

# Scope of the Project

## In scope

- A console based menu driven application developed in Python.
- Expense(category, value, date) as in the example.
- All of the recorded expenses can be seen in a formatted table.
- Generating a category-wise total spending summary.
- How to quickly recover from invalid menu inputs and empty-data cases.
- Modular code – separate modules to add, view and summarise expenses. You should be able to create any number of such modules in the system that you develop, but you need to have at least 3 modules.

## Out of scope (current version)

- Permanent storage (the data remains in the memory until closing the session).
- User accounts / login and multi-user support.
- Graphical or web interface.
- Editing or deleting existing expenses.
- Budget limits, alerts and charts.

# Target Users

- Students who are handling their own pocket money or allowance on a monthly basis.
- For people who seek a fast, easy method to track daily expenses.
- For beginners interested in getting to grips with a small, modular Python project.

# High-Level Features

1. Add Expense – We capture category, amount and date of an Expense.
2. View Expenses - show all expenses in a tabular format, formatted so they are in order.
3. Cost Breakdowns – group your costs by type and display the total amount you spent on a specific type of cost.
4. Interactive menu - a menu based on looping with input validation and a very clean exit.
5. Modular Design - everything in separate files (add_exp.py, view.py, summary.py) with main.py coordinating the execution.