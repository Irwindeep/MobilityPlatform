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
    if len(sys.argv) != 4:
        print("Bad Credentials, terminating the program")
        print(sys.argv)
        exit(1)
    name = sys.argv[1]
    uid = sys.argv[2]
    selection = sys.argv[3]
    
    print(f"Recieved Values\nName: {name}\nUID: {uid}\nSelection: {selection}")

    #key = base64.urlsafe_b64decode(key_str)
    #if is_valid_key(key) == False:
    #    print("Some undefined error occured, terminating the program")
    #    exit(-1)
    #name = decrypt_data(name, key)
    #uid = decrypt_data(uid, key)
    #selection = decrypt_data(selection, key)
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
    linkedlist = Cycles()
    with open("/home/Host/Project/cycles.txt", "r") as file:
        for line in file:
            elements = line.split()
            name = elements[0]
            avail = elements[1]
            linkedlist.append(name, avail)
    current = linkedlist.head
    while current != None:
        if current.name == selection:
            break
        current = current.next
    current.isAvail = False
    linkedlist.update()
    data = f"Thanks for the purchase\n{n} is your passkey for the chosen bicycle"
    print(data)
