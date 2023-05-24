import rsa
import os
from termcolor import colored
from prettytable import PrettyTable

def main():
    # Prints a blue table with the title "Cryptography Tool" and "RSA ENCRYPTOR/DECRYPTOR"
    print("\n\n")
    a = PrettyTable()
    a.field_names = ["RSA Tool"]
    a.add_row(["ENCRYPTOR & DECRYPTOR"])
    print(colored(a, 'blue'))

     # Prompts the user to choose between encryption or decryption
    choice = input("\nWould you like to encrypt or decrypt? (e/d) ")

    if choice == "e":   #encryption
        # Prompts the user to enter the path of the plaintext file to encrypt
        plaintext_path = input("\nEnter the path of the plaintext file: ")
        # Reads the plaintext from the file
        with open(plaintext_path, 'r') as file:
            plaintext = file.read()

        # Generates a new key pair
        (pubkey, privkey) = rsa.newkeys(2048)
        # Prompts the user to enter a name for the key pair
        key_name = input("\nEnter a name for the key pair: ")
        # Stores the key pair
        store_key(pubkey, privkey, key_name)
        
        print(colored("Encrypting the message...\n", 'green'))
        # Encrypts the plaintext using the public key
        ciphertext = rsa.encrypt(plaintext.encode('ascii'), pubkey)

        cipher_name = input("Enter the name of the ciphertext file: ")
        # Saves the ciphertext to a file
        save_ciphertext(ciphertext, cipher_name)

        print(colored("Encryption Successful!\n", 'green'))

        print(colored("Signing the message...\n", 'blue'))
        # Signs the plaintext using the private key
        signature = sign(plaintext, privkey)

        # Prompts the user to enter a name for the signature file
        sign_name = input("Enter the name of the signature file:  ")
        # Saves the signature to a file
        save_signature(signature, sign_name)

        print(colored("Message Signed\n", 'blue'))
        
    elif choice == "d":    #decryption
        # Prompts the user to enter the name of the key pair to use
        key_name = input("\nEnter the name of the key pair to use: ")
        # Retrieves the key pair
        (pubkey, privkey) = retrieve_key(key_name)

        # Prompts the user to enter the name of the ciphertext file to decrypt
        cipher_name = input("\nEnter the name of the ciphertext file to decrypt: ")
       
        #Using try-except for error handling
        try:
            # Retrieves the ciphertext from the file
            ciphertext = retrieve_cipher(cipher_name)
            print(colored("Decrypting...\n", 'green'))
            # Decrypts the ciphertext using the private key
            plaintext = rsa.decrypt(ciphertext, privkey).decode('ascii')
            # Creates a table with the decrypted plaintext
            x = PrettyTable()
            x.field_names = ["Plaintext"]
            x.add_row([plaintext])
            print(colored(x, 'green'))

            # Prompts the user to enter the name of the signature file to verify
            sign_name = input("\nEnter the name of the signature file to verify: ")
            # Retrieves the signature from the file
            signature = retrieve_signature(sign_name)

            # Verifies the signature using the plaintext and public key
            if verify(plaintext, signature, pubkey):
                # Prints that the signature was successfully verified
               print(colored('\nSuccessfully verified signature\n', 'green'))
            else:
                # Prints that the signature could not be verified
                print(colored('\nThe message signature could not be verified\n', 'red'))

        except:
            print(colored('\nThe ciphertext could not be decrypted. Check your keys and try again.\n', 'red'))

    else:
        # Prints an error message if the choice is not "e" or "d"
        print(colored("\nInvalid choice\n", 'red'))

# Function to store a key pair to files
def store_key(pubkey, privkey, key_name):
    # Creates a directory for the keys if it doesn't exist
    if not os.path.exists('keys'):
        os.makedirs('keys')

    # Writes the public key to a file
    with open(f'keys/{key_name}_pubkey.pem', 'wb') as f:
        f.write(rsa.PublicKey.save_pkcs1(pubkey))
    # Writes the private key to a file
    with open(f'keys/{key_name}_privkey.pem', 'wb') as f:
        f.write(rsa.PrivateKey.save_pkcs1(privkey))

# Function to retrieve a key pair from files
def retrieve_key(key_name):
    # Reads the public key from a file
    with open(f'keys/{key_name}_pubkey.pem', 'rb') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())
    # Reads the private key from a file
    with open(f'keys/{key_name}_privkey.pem', 'rb') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())
    return (pubkey, privkey)

# Function to save ciphertext to a file
def save_ciphertext(ciphertext, cipher_name):
    # Creates a directory for the ciphertext if it doesn't exist
    if not os.path.exists('cipher'):
        os.makedirs('cipher')
    # Writes the ciphertext to a file
    with open(f'cipher/{cipher_name}', 'wb') as file:
        file.write(ciphertext)

# Function to retrieve ciphertext from a file
def retrieve_cipher(cipher_name):
    with open(f'cipher/{cipher_name}', 'rb') as file:
        ciphertext = file.read()
    return ciphertext

# Function to sign plaintext using private key
def sign(plaintext, key):
    return rsa.sign(plaintext.encode('ascii'), key, 'SHA-1')

# Function to save signature to a file
def save_signature(signature, sign_name):
    if not os.path.exists('signature'):
        os.makedirs('signature')
    with open (f'signature/{sign_name}', 'wb') as file:
        file.write(signature)

# Function to retrieve signature from a file
def retrieve_signature(sign_name):
    with open(f'signature/{sign_name}', 'rb') as file:
            signature = file.read()
    return signature

# Function to verify signature using plaintext and public key
def verify(plaintext, signature, key):
    try:
        return rsa.verify(plaintext.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False

if __name__ == "__main__":
    main()  #calling the main function
