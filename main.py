# ========= main.py ================
# Test script for the Account class. Uses a sentinel-controlled loop
# to create, search, display, and save accounts.
# Input: User input via console
# Output: Printed output and saved data to file
# ====================================

from account import Account

def green(text):
    return f"\033[92m{text}\033[0m"  # Green
def red(text):
    return f"\033[91m{text}\033[0m"  # Red
def yellow(text):
    return f"\033[93m{text}\033[0m"  # Yellow

def main():
    # Create an Account instance with default values
    account_manager = Account("default", "default")

    # Load accounts from file at program start
    account_manager.loadAccountsFromFile("accounts.txt")

    choice = -1  # Sentinel value

    while choice != 0:
        print("\n" + "="*30)
        print("        ACCOUNT MENU")
        print("="*30)
        account_manager.displayMenu()
        print("="*30)

        try:
            choice = int(input("Enter your choice (0 to quit): "))
        except ValueError:
            print(red("Invalid input. Please enter a number.\n"))
            continue

        if choice == 1:
            website = input("\nEnter website name: ")
            username = input("Enter username: ")
            action = account_manager.handleChoices(choice)
            action(website, username)

        elif choice == 2:
            website = input("\nEnter website to search: ")
            action = account_manager.handleChoices(choice)
            result = action(website)
            print(green(result) if "does not" not in result else red(result))

        elif choice == 3:
            action = account_manager.handleChoices(choice)
            action()

        elif choice == 0:
            print(yellow("\nSaving accounts and exiting..."))
            account_manager.saveAccountToFile("accounts.txt")
            print(green("Accounts saved. Goodbye!\n"))

        else:
            print(red("Invalid choice. Please try again.\n"))

# Run the program
if __name__ == "__main__":
    main()
