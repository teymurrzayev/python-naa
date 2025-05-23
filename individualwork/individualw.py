import json
import time

accounts = []

def welcome_screen():
    ascii_art = r"""
    ***************************************
    *     WELCOME TO BANKING SYSTEM       *
    *     Designed by Teymur Rzayev       *
    ***************************************
    """
    print(ascii_art)
    time.sleep(2)

def main_menu():
    print("""
    ====== MAIN MENU ======
    1. Add New Account
    2. View All Accounts
    3. Search Account
    4. Deposit Money
    5. Withdraw Money
    6. Delete Account
    7. Show Summary Stats
    8. Save to File
    9. Load from File
    10. Sort Accounts
    11. Recursive Account Count
    12. Clear All Data
    0. Exit
    =======================
    """)

def add_account():
    try:
        account = {
            "id": input("Enter Account ID: ").strip(),
            "name": input("Enter Account Holder Name: ").strip(),
            "balance": float(input("Enter Initial Balance: "))
        }
        if any(acc["id"] == account["id"] for acc in accounts):
            print("Account ID already exists!")
            return
        accounts.append(account)
        print("Account successfully added.")
    except ValueError:
        print("Invalid input! Balance must be a number.")

def view_accounts():
    if not accounts:
        print("No accounts found.")
        return
    print("{:<10}{:<20}{:<10}".format("ID", "Name", "Balance"))
    for acc in accounts:
        print("{:<10}{:<20}{:<10.2f}".format(acc["id"], acc["name"], acc["balance"]))

def search_account():
    aid = input("Enter Account ID to search: ")
    for acc in accounts:
        if acc["id"] == aid:
            print("Account Found:", acc)
            return
    print("Account not found.")

def deposit_money():
    aid = input("Enter Account ID to deposit into: ")
    for acc in accounts:
        if acc["id"] == aid:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    acc["balance"] += amount
                    print("Deposit successful.")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid amount.")
            return
    print("Account not found.")

def withdraw_money():
    aid = input("Enter Account ID to withdraw from: ")
    for acc in accounts:
        if acc["id"] == aid:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= acc["balance"]:
                    acc["balance"] -= amount
                    print("Withdrawal successful.")
                else:
                    print("Invalid amount or insufficient funds.")
            except ValueError:
                print("Invalid amount.")
            return
    print("Account not found.")

def delete_account():
    aid = input("Enter Account ID to delete: ")
    for i, acc in enumerate(accounts):
        if acc["id"] == aid:
            del accounts[i]
            print("Account deleted.")
            return
    print("Account not found.")

def summary_stats():
    if not accounts:
        print("No data to show.")
        return
    total_balance = sum(acc["balance"] for acc in accounts)
    avg_balance = total_balance / len(accounts)
    print(f"Total Accounts: {len(accounts)}")
    print(f"Total Balance: {total_balance:.2f}")
    print(f"Average Balance: {avg_balance:.2f}")

def save_to_file():
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)
    print("Accounts saved to file.")

def load_from_file():
    global accounts
    try:
        with open("accounts.json", "r") as f:
            accounts = json.load(f)
        print("Accounts loaded from file.")
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("File is corrupted or invalid format.")

def sort_accounts():
    key = input("Sort by 'id', 'name', or 'balance': ").strip()
    if key in ["id", "name", "balance"]:
        accounts.sort(key=lambda acc: acc[key])
        print(f"Accounts sorted by {key}.")
    else:
        print("Invalid field.")

def recursive_count(index=0):
    if index >= len(accounts):
        return 0
    return 1 + recursive_count(index + 1)

def clear_data():
    confirm = input("Are you sure to delete all accounts? (yes/no): ").lower()
    if confirm == "yes":
        accounts.clear()
        print("All data cleared.")
    else:
        print("Cancelled.")

def help_menu():
    print("""
    INSTRUCTIONS:
    - Account ID must be unique.
    - Use option 8 to save and option 9 to load your data.
    - You can sort accounts by ID, name, or balance.
    - Deposits must be positive. Withdrawals cannot exceed balance.
    """)

def main():
    welcome_screen()
    while True:
        main_menu()
        try:
            choice = input("Choose an option: ").strip()
            match choice:
                case "1":
                    add_account()
                case "2":
                    view_accounts()
                case "3":
                    search_account()
                case "4":
                    deposit_money()
                case "5":
                    withdraw_money()
                case "6":
                    delete_account()
                case "7":
                    summary_stats()
                case "8":
                    save_to_file()
                case "9":
                    load_from_file()
                case "10":
                    sort_accounts()
                case "11":
                    print(f"Total accounts: {recursive_count()}")
                case "12":
                    clear_data()
                case "0":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Try again.")
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
