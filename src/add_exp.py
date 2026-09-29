def add_exp(exp_list):  
    print("\t----add New Expense----")
    cat = input("Enter category(e.g.,Food,Travel): ")

    amt = input("Enter amount: ")
    amount=int(amt)

    date=input("Enter date(DD-MM-YYYY): ")

    exp=(cat,amount, date)

    exp_list.append(exp)
    print("Expense added successfully.")
