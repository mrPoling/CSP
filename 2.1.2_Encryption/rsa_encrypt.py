#   a212_rsa_encrypt.py
import rsa as rsa
import read_file as rf

num = (input("Enter the Encryption Key: " ))
while (len(num) < 4 or not num.isdigit()):
    num = (input("Key must be an integer (4-5 digits)\nEnter the Encryption Key: " ))
key = int(num)

num = (input("Enter the Modulus: " ))
while (len(num) < 4 or not num.isdigit()):
    num = (input("Modulus must be an integer (4-5 digits)\nEnter the Modulus Key: " ))
mod_value = int(num)

plaintext = input("Enter a message to encrypt OR type 'file'\n")

if (plaintext == "file"):
    filename = "input_message"
    print("Ok, reading input message from file '" + filename + "'")
    plaintext = ", ".join(rf.get_file_firstline(filename))
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
    
print("Encrypted Message:\n")
print(*encrypted_msg, sep=", ", end="\n\n") #Print without brackets
