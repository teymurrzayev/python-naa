import json

accounts = []

def main_menu():
    print("""
    ====== SIMPLE BANKING SYSTEM ======
    1. Add New Account
    2. View All Accounts
    3. Search Account
    4. Deposit
    5. Withdraw
    6. Delete Account
    7. Summary Stats
    8. Save to File
    9. Load from File
    0. Exit
    ===================================
    """)

def add_account():
    try:
        account = {
            "id": input("Enter account ID: "),
            "name": input("Enter account holder name: "),
            "balance": float(input("Enter initial balance: "))
        }
        accounts.append(account)
        print("Account added successfully.")
    except ValueError:
        print("Invalid input! Balance must be a number.")

def view_accounts():
    if not accounts:
        print("No accounts found.")
    else:
        print("{:<10}{:<20}{:<10}".format("ID", "Name", "Balance"))
        for a in accounts:
            print("{:<10}{:<20}{:<10.2f}".format(a["id"], a["name"], a["balance"]))

def search_account():
    aid = input("Enter account ID to search: ")
    for a in accounts:
        if a["id"] == aid:
            print("Account Found:", a)
            return
    print("Account not found.")

def deposit():
    aid = input("Enter account ID to deposit to: ")
    for a in accounts:
        if a["id"] == aid:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    a["balance"] += amount
                    print("Deposit successful.")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid amount.")
            return
    print("Account not found.")

def withdraw():
    aid = input("Enter account ID to withdraw from: ")
    for a in accounts:
        if a["id"] == aid:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= a["balance"]:
                    a["balance"] -= amount
                    print("Withdrawal successful.")
                else:
                    print("Invalid amount or insufficient balance.")
            except ValueError:
                print("Invalid amount.")
            return
    print("Account not found.")

def delete_account():
    aid = input("Enter account ID to delete: ")
    for i, a in enumerate(accounts):
        if a["id"] == aid:
            del accounts[i]
            print("Account deleted.")
            return
    print("Account not found.")

def summary_stats():
    if not accounts:
        print("No accounts to summarize.")
        return
    total = sum(a["balance"] for a in accounts)
    avg = total / len(accounts)
    print(f"Total accounts: {len(accounts)}")
    print(f"Total balance: {total:.2f}")
    print(f"Average balance: {avg:.2f}")

def save_to_file():
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)
    print("Data saved to accounts.json")

def load_from_file():
    global accounts
    try:
        with open("accounts.json", "r") as f:
            accounts = json.load(f)
        print("Data loaded from file.")
    except FileNotFoundError:
        print("No file found.")
    except json.JSONDecodeError:
        print("File is corrupted.")

def main():
    while True:
        main_menu()
        choice = input("Choose an option: ")
        match choice:
            case "1": add_account()
            case "2": view_accounts()
            case "3": search_account()
            case "4": deposit()
            case "5": withdraw()
            case "6": delete_account()
            case "7": summary_stats()
            case "8": save_to_file()
            case "9": load_from_file()
            case "0":
                print("Goodbye!")
                break
            case _: print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
