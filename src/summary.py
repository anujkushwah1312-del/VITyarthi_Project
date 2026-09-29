def summary(exp_list):
    print("\t----Expense Summary----")
    if not exp_list:
        print("No data!")
        return

    summ_dic={}

    for exp in exp_list:
        category=exp[0]
        amount=exp[1]

        if category in summ_dic:
            summ_dic[category] += amount
        else:
            summ_dic[category] = amount

    for category, total in summ_dic.items():
        print(f"-->{category}: Rs.{total}")
        print("-"*32)