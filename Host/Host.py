import sys
import os
import random
from datetime import datetime
from cryptography.fernet import Fernet
import base64
from cycles import *

    
def decrypt_data(data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(data).decode()
    return decrypted_data

def is_valid_key(key):
    try:
        # Decode the key to check its length
        decoded_key = base64.urlsafe_b64decode(key)
        # Check if the length of the decoded key is 32 bytes
        return len(decoded_key) == 32
    except (ValueError, TypeError):
        return False

if __name__=="__main__":
    if len(sys.argv) != 5:
        print("Bad Credentials, terminating the program")
        exit(1)
    name = sys.argv[1]
    uid = sys.argv[2]
    selection = sys.argv[3]
    key_str = sys.argv[4]
    
    name = base64.urlsafe_b64decode(name)
    uid = base64.urlsafe_b64decode(uid)
    selection = base64.urlsafe_b64decode(selection)

    key = base64.urlsafe_b64decode(key_str)
    if is_valid_key(key) == False:
        print("Some undefined error occured, terminating the program")
        exit(-1)
    name = decrypt_data(name, key)
    uid = decrypt_data(uid, key)
    selection = decrypt_data(selection, key)
    file_path = f"/home/Host/Project/Registrations/{uid}.txt"
    n = random.randint(1000, 9999)
    try:
        with open(file_path, "a") as file:
            file.write(f"{datetime.now()}: {name} {selection} {n}\n")
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write(f"{datetime.now()}: {name} {selection} {n}\n")
    except Exception as e:
        print(f"An error occured: {e}")
        exit(2)
    with open("/home/Host/Project/cycles.txt", "r") as file:
        for line in file:
            elements = line.split()
            name = elements[0]
            avail = elements[1]
            cycles.append(name, avail)
    current = cycles.head
    with open("/home/Host/Project/cycles.txt", "w") as file:
        while current != None:
            if current.name == selection:
                current.isAvail = False
            avail = ""
            if current.isAvail == True:
                avail = "Available"
            else:
                avail = "Not_Available"
            file.write(f"{current.name} {avail}\n")
            current = current.next
    data = f"Thanks for the purchase\n{n} is your passkey for the chosen bicycle"
    print(data)
    
