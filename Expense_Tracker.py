mount=400
category="Food"
description="Lunch"
print("Amo..",amount)
print("Cate..",category)
print("Descri...",description)

print("Take input from user")
amount=int(input("Enter ammount:"))
category=input("Enter category:")
description=input("Enter description:")
print(amount)
print(category)
print(description)

print("Store Multiple expenses")
expenses=[]
expenses.append({
    "amount":500,
    "Category":"food",
    "description":"Lunch"
})
expenses.append({
    "amount": 1000,
    "category": "Transport",
    "description": "Uber"
})

expenses.append({
         "amount":3000,
         "category":"house",
         "description":" 3 Kanal"
})
print(expenses)
expenses = []


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    add_expense()
def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses:", total)

while True:

    print("%%%%%%")
    print("1. Add Expense")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()


    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("bye")
        break

    else:
        print("wrong")