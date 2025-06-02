class Account:
    # ========= __init__ ================
    # Constructor to initialize username, password, and the accounts dictionary.
    # Input: username (str), password (str)
    # Output: None
    # ====================================
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.accounts = {}

    # ========= __repr__ ================
    # Returns an unambiguous string representation of the object.
    # Input: None
    # Output: str
    # ====================================
    def __repr__(self) -> str:
        return f"Account(username={self.username!r}, password={self.password!r})"
    
    # ========= __str__ ================
    # Returns a user-friendly string representation of the object.
    # Input: None
    # Output: str
    # ====================================
    def __str__(self) -> str:
        return f"Account with username: {self.username} and password: {self.password}"

    # ========= displayMenu ================
    # Displays a menu of options to the user.
    # Input: None
    # Output: None
    # ====================================
    def displayMenu(self) -> None:
        print("1. Create Account")
        print("2. Search for Account")
        print("3. Display all accounts")    
        print("0. Exit")
        print("Please select an option (0-3):")

    # ========= handleChoices ================
    # Handles user menu choice and returns the corresponding method.
    # Input: choice (int)
    # Output: function or fallback lambda
    # ====================================
    def handleChoices(self, choice: int) -> callable:
        switcher = {
            1: self.addAccount,
            2: self.getAccount,
            3: self.displayAllAccounts,
            4: self.updatePassword
        }
        return switcher.get(choice, lambda *args: print("Invalid choice"))

    # ========= addAccount ================
    # Adds a new account with a generated secure password.
    # Input: website (str), username (str)
    # Output: None
    # ====================================
    def addAccount(self, website: str, username: str) -> None:
        try:
            if website in self.accounts:
                print(f"{website} already exists. Please choose a different website.")
                return
            else:
                password = self.generateSecurePassword()
                self.accounts[website] = {"username": username, "password": password}
                print(f"Account added for {website}: Username = {username}, Password = {password}")

                # Save to file immediately
                self.saveAccountToFile("accounts.txt")

        except Exception as e:
            print(f"Error adding account: {e}")

        
    # ========= getAccount ================
    # Retrieves an account's info based on website.
    # Input: website (str)
    # Output: str
    # ====================================
    def getAccount(self, website: str) -> str:
        try:
            if website in self.accounts:
                info = self.accounts[website]
                return f"Website: {website}, Username: {info['username']}, Password: {info['password']}"
            else:
                return f"Account for {website} does not exist."
        except Exception as e:
            return f"Error retrieving account: {e}"
    
    # ========= displayAllAccounts ================
    # Displays all stored accounts in the accounts dictionary.
    # Input: None
    # Output: None
    # ====================================
    def displayAllAccounts(self) -> None:
        if not self.accounts:
            print("No accounts stored.")
            return
        print("{:<20} | {:<20} | {:<20}".format("Website", "Username", "Password"))
        print("-" * 65)
        for website, data in self.accounts.items():
            print("{:<20} | {:<20} | {:<20}".format(website, data['username'], data['password']))

    # ========= getUsername ================
    # Returns the current username of this Account object.
    # Input: None
    # Output: str
    # ====================================
    def getUsername(self) -> str:
        return self.username
    
    # ========= getPassword ================
    # Returns the current password of this Account object.
    # Input: None
    # Output: str
    # ====================================
    def getPassword(self) -> str:
        return self.password
    
   
    # ========= saveAccountToFile ================
    # Overwrites all accounts to the specified file.
    # Input: filename (str)
    # Output: bool (True if saved successfully, False if an error occurred)
    # ====================================
    def saveAccountToFile(self, filename: str) -> bool:
        try:
            with open(filename, "w") as file:
                for website, data in self.accounts.items():
                    file.write(f"{website} {data['username']} {data['password']}\n")
            print(f"Accounts saved to {filename} successfully.")
            return True
        except Exception as e:
            print(f"Error saving accounts to file: {e}")
            return False

    # ========= loadAccountsFromFile ================
    # Loads accounts from the specified file into the accounts dictionary.
    # Input: filename (str)
    # Output: bool (True if loaded successfully, False if an error occurred)
    # ================================================
    def loadAccountsFromFile(self, filename: str) -> bool:
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 3:
                        website, username, password = parts
                        self.accounts[website] = {"username": username, "password": password}
            print(f"\033[92mAccounts loaded from {filename}.\033[0m")
            return True
        except FileNotFoundError:
            print(f"\033[93m{filename} not found. Starting with empty account list.\033[0m")
            return True  # Not a critical failure
        except Exception as e:
            print(f"\033[91mError loading accounts from file: {e}\033[0m")
            return False            

    # ========= generateSecurePassword ================
    # Generates a secure password following specific criteria.
    # Input: None
    # Output: str (the generated password)
    # =================================================
    def generateSecurePassword(self) -> str:
        try:
            from secrets import choice
            res = ""

            uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
            digits = "0123456789"
            specialCharacters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
            allCharacters = uppercaseLetters + lowercaseLetters + digits + specialCharacters

            res += choice(uppercaseLetters)
            res += choice(lowercaseLetters)
            res += choice(digits)
            res += choice(specialCharacters)

            for _ in range(11):  # total 15 characters
                res += choice(allCharacters)

            res = ''.join(choice(res) for _ in range(len(res)))

            print(f"Generated secure password: {res}")
            return res
        except Exception as e:
            print(f"Error generating secure password: {e}")
            return "defaultPassword123!"

    # ========= updataPassword ================
    # Updates the password for a given website by generating a new secure password.
    # Input: website (str)
    # Output: Bool (True if updated successfully, False if an error occurred)
    # ========================================
    def updatePassword(self, website: str) -> bool:
        try:
            if website in self.accounts:
                newPassword = self.generateSecurePassword()
                self.accounts[website]['password'] = newPassword
                print(f"Password for {website} updated successfully.")
                return True
            else:
                print(f"Account for {website} does not exist.")
                return False
        except Exception as e:
            print(f"Error updating password: {e}")
            return False

__all__ = ["Account"]
