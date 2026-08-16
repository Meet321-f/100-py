name  = input("Enter Your Name : ")
budget = float(input("Enter Your Budget : "))

expense_count  = int(input("Enter Number of Expenses : "))

print(f"Name : {name}")
print(f"Budget : ₹{budget}")
print(f"Number of Expenses : {expense_count}")

expenses = []

for i in range(expense_count):
    print(f"\nExpense {i + 1}")
             
    expense_name = input(f"Enter Your Expense {i + 1} Name : ")
    expense_category = input(f"Enter {expense_name} Category : ")
    expense_amount = float(input(f"Enter {expense_name} Amount : ₹"))


    expenses.append({
        "name": expense_name,
        "category": expense_category,
        "amount": expense_amount
    })

total_expense = 0

for expense in expenses:
    total_expense += expense["amount"]

remaining = budget - total_expense

print("\n========== EXPENSES ==========")

for expense in expenses:
    print(
        f"{expense['name']} | "
        f"{expense['category']} | "
        f"₹{expense['amount']}"
    )

print("============summary============")
print(f"Name : {name}")
print(f"Budget : ₹{budget}")
print(f"Total Expense : ₹{total_expense}")
print(f"Remaining : ₹{remaining}")
