from src.add_exp import add_exp
from src.view import view
from src.summary import summary

def main():
    master_exp_list=[]

    while True:
        print("\t====Expense Tracker=====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_exp(master_exp_list)
        elif choice == '2':
            view(master_exp_list)
        elif choice == '3':
            summary(master_exp_list)
        elif choice == '4':
            print("Thank YOU!")
            break
        else:
            print("Invalid choice! Enter choice (1-4): ")

if __name__ == "__main__":
    main()  