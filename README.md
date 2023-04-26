# RSA_Encryptor_Decryptor

This code is an implementation of the RSA encryption and decryption algorithm. This program allows a user to encrypt and decrypt a plaintext file using the RSA encryption algorithm. The user can also sign and verify the plaintext file using the RSA signature algorithm. The script uses the RSA library and the PrettyTable library to display the results in a table format. The user is prompted to choose between encryption or decryption and is then prompted for various input such as the plaintext file path, the key pair name, and the ciphertext and signature file names.

The program works as follows:

1. The user is prompted to choose between encryption or decryption.

2. If the user chooses encryption: The user is prompted to enter the path of the plaintext file to encrypt, The plaintext is read from the file, A new RSA key pair is generated, The user is prompted to enter a name for the key pair, The key pair is stored in the operating system, The plaintext is encrypted using the public key, The user is prompted to enter a name for the ciphertext file, The ciphertext is saved to a file, The plaintext is signed using the private key, The user is prompted to enter a name for the signature file, The signature is saved to a file.
  
3. If the user chooses decryption: The user is prompted to enter the name of the key pair to use, The key pair is retrieved from the operating system, The user is prompted to enter the name of the ciphertext file to decrypt, The ciphertext is retrieved from the file, The ciphertext is decrypted using the private key, The plaintext is displayed in a table, The user is prompted to enter the name of the signature file to verify, The signature is retrieved from the file, The signature is verified using the plaintext and public key, The results of the verification are displayed.
