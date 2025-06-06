# 🔐 Password Manager CLI

A simple terminal-based **Password Manager** built with Python. It allows users to:

- Create secure accounts associated with websites
- Auto-generate strong passwords
- View and search stored accounts
- Save and load credentials to/from a file (`accounts.txt`)

---

## 🛠️ How It Works

1. On startup, the program loads all saved accounts from `accounts.txt`.
2. User interacts with a menu:
   - `1` to create a new account
   - `2` to search for a saved website
   - `3` to display all accounts
   - `0` to quit and save data
3. Each created account is saved immediately to `accounts.txt`.

---

## 📦 Requirements

- Python 3.x
- No external libraries required (uses built-in modules like `secrets`)

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/avilla212/password-manager-cli.git

# Navigate into the project directory
cd password-manager-cli

# Run the application
python main.py
