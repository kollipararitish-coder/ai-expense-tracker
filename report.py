import matplotlib.pyplot as plt

def generate_report(expenses):

    total = {}

    for category, amount in expenses:

        if category not in total:
            total[category] = 0

        total[category] += amount

    print("\nMonthly Expense Report")

    for k, v in total.items():
        print(k, ":", v)

    categories = list(total.keys())
    values = list(total.values())

    plt.bar(categories, values)

    plt.title("Expense Report")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()