transactions = [
    {"name": "Laptop", "amount": 250000, "type": "expense"},
    {"name": "Salary", "amount": 500000, "type": "income"},
    {"name": "Internet", "amount": 30000, "type": "expense"},
    {"name": "Freelance", "amount": 150000, "type": "income"},
    {"name": "Food", "amount": 45000, "type": "expense"}
]

def total_income(transactions):
    total= 0
    for transaction in transactions:
        for key, value in transaction.items():
            if key == "type" and value == "income":
                total += transaction.get("amount", 0)

    return [f"Total income: {total}", total]
        
def total_expenses(transactions):
    total= 0
    for transaction in transactions:
        for key, value in transaction.items():
            if key == "type" and value == "expense":
                total += transaction.get("amount", 0)
   
    return [f"Total expenses: {total}", total]

def balance(transactions):
    return total_income(transactions)[1]-total_expenses(transactions)[1]
    
def largest_expense(transactions):
    largest = ""
    amount = 0

    for transaction in transactions:
        for key, value in transaction.items():
            if key == "type" and value == "expense":
                if (new:=transaction.get("amount", 0)) > amount: 
                    amount = new
                    largest = transaction.get("name", "")
    return f"Largest expense: {largest} ({amount})"

def num_of_expense(transactions):
    num= 0
    for transaction in transactions:
        for key, value in transaction.items():
            if key == "type" and value == "expense":
                num += 1
    return f"Number of expenses: {num}"

def status(transactions):
    if balance(transactions) > 0:
        return "Status: Positive balance"
    return "Status: Negative balance"


print(total_income(transactions)[0])
print(total_expenses(transactions)[0])
print(balance(transactions))
print(largest_expense(transactions))
print(num_of_expense(transactions))
print(status(transactions))
