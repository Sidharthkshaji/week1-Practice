expenses = [250, 1200, 450, 800, 150, 2000, 350]

total_expense = sum(expenses)
average_expense = total_expense/len(expenses)
highest_expense = max(expenses)
lowest_expense = min(expenses)
expense_above = 0
expense_below = 0
for i in expenses:
    if i >500:
        expense_above += 1
    else:
        expense_below += 1
print("Total Expenses:",total_expense)
print(f"Average Expense:, {average_expense:.2f}")
print("Highest Expense:",highest_expense)
print("Lowest Expense:",lowest_expense)
print("Number of expenses Above ₹500:",expense_above)
print("Number of expenses below or equal ₹500 :",expense_below)