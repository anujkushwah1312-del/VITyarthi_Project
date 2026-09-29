def view(exp_list):
    print("\t====ALL EXPENSES====")
    if not exp_list:
        print("No expenses recorded.")
        return

    print(f"{'Category':<15} | {'Amount':<10} | {'Date':<12}")
    print("-"*45)

    for exp in exp_list:
        print(f"{exp[0]:<15} | {exp[1]:<10} | {exp[2]:<12}")
        print("-"*45)
