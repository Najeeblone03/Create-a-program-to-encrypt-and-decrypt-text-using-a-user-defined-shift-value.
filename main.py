history = []


def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - start + shift) % 26 + start)
        else:
            result += ch
    return result


while True:
    print("\n===== ADVANCED CAESAR CIPHER =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force Attack")
    print("4. Save Last Result")
    print("5. View History")
    print("6. Encrypt Text File")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter key: "))
        result = caesar(text, shift)
        print("Encrypted:", result)
        history.append(("Encrypt", result))

    elif choice == "2":
        text = input("Enter text: ")
        shift = int(input("Enter key: "))
        result = caesar(text, -shift)
        print("Decrypted:", result)
        history.append(("Decrypt", result))

    elif choice == "3":
        text = input("Enter encrypted text: ")
        print("\nPossible Decryptions:")
        for key in range(26):
            print(f"Key {key}: {caesar(text, -key)}")

    elif choice == "4":
        try:
            with open("cipher_output.txt", "w") as f:
                f.write(result)
            print("Saved to cipher_output.txt")
        except:
            print("No result available.")

    elif choice == "5":
        print("\nHistory:")
        for i, item in enumerate(history, 1):
            print(i, item[0], ":", item[1])

    elif choice == "6":
        filename = input("Enter file name: ")
        shift = int(input("Enter key: "))
        try:
            with open(filename, "r") as f:
                data = f.read()

            encrypted = caesar(data, shift)

            with open("encrypted_file.txt", "w") as f:
                f.write(encrypted)

            print("Encrypted file saved as encrypted_file.txt")

        except FileNotFoundError:
            print("File not found.")

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
