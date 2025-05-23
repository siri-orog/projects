from cryptography.fernet import Fernet

# Generate and save an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")

# Load the saved key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filename + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{filename}' encrypted successfully!")

# Decrypt a file
def decrypt_file(encrypted_filename):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_filename = encrypted_filename.replace(".encrypted", "")
    with open(original_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File '{encrypted_filename}' decrypted successfully!")

# Menu-driven interface
def main():
    print("\nFile Encryption/Decryption Tool")
    print("1. Generate Encryption Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        filename = input("Enter the filename to encrypt: ")
        encrypt_file(filename)
    elif choice == "3":
        encrypted_filename = input("Enter the filename to decrypt: ")
        decrypt_file(encrypted_filename)
    else:
        print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()