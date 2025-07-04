class apiKey:
    def __init__(self, key: str):
        self.keyMap = {}
        self.key = key
        self.keyMap[key] = None
    
    def addKey(self, keyName: str, keyValue: str) -> None:
        try:
            if keyName in self.keyMap:
                raise ValueError(f"Key '{keyName}' already exists.")
            self.keyMap[keyName] = keyValue


            print(f"Key '{keyName}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def writeKeysToFile(self, fileName: str) -> None:
        try:
            with open(fileName, 'w') as file:
                for keyName, keyValue in self.keyMap.items():
                    file.write(f"{keyName}:{keyValue}\n")
        except FileNotFoundError:
            print(f"File '{fileName}' not found. Creating a new file.")
            with open(fileName, 'w') as file:
                for keyName, keyValue in self.keyMap.items():
                    file.write(f"{keyName}:{keyValue}\n")
        except Exception as e:
            print(f"Error writing keys to file: {e}")
    
    def loadKeysFromFile(self, fileName: str) -> None:
        try:
            with open(fileName, 'r') as file:
                for line in file:
                    keyName, keyValue = line.strip().split(':')
                    self.keyMap[keyName] = keyValue
        except FileNotFoundError:
            print(f"File '{fileName}' not found. No keys loaded.")
        except Exception as e:
            print(f"Error loading keys from file: {e}")
    
    def displayKeys(self) -> None:
        if not self.keyMap:
            print("No keys available.")
            return
        print("Available API Keys:")
        for keyName, keyValue in self.keyMap.items():
            print(f"{keyName}: {keyValue if keyValue else 'No value assigned'}")


if __name__ == "__main__":
    api = apiKey("default_key")
    fileName = "api_keys.txt"

    key = ""
    sentinel = -1

    print("Welcome to the API Key Manager!")
    print("1. Add API Key")
    print("2. Write Keys to File")
    print("3. Load Keys from File")
    print("4. Display Keys")

    while sentinel != 0:
        try:
            sentinel = int(input("Enter your choice (0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if sentinel == 1:
            keyName = input("Enter key name: ")
            keyValue = input("Enter key value: ")
            api.addKey(keyName, keyValue)

        elif sentinel == 2:
            fileName = input("Enter file name to write keys: ")
            api.writeKeysToFile(fileName)

        elif sentinel == 3:
            fileName = input("Enter file name to load keys from: ")
            api.loadKeysFromFile(fileName)

        elif sentinel == 4:
            api.displayKeys()

        elif sentinel == 0:
            print("Exiting the API Key Manager. Goodbye!")
            api.writeKeysToFile(fileName)
        
        else:
            print("Invalid choice. Please try again.")


    