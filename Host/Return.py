import sys
from cryptography.fernet import Fernet
import base64
from cycles import *

def decrypt_data(data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(data).decode()
    return decrypted_data

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Bad Credentials, terminating the program")
		exit(1)
	uid_str = sys.argv[1]
	key_str = sys.argv[2]
	otp_str = sys.argv[3]
	
	uid = base64.urlsafe_b64decode(uid_str)
	otp = base64.urlsafe_b64decode(otp_str)
	key = base64.urlsafe_b64decode(key_str)
	
	uid = decrypt_data(uid, key)
	otp = decrypt_data(otp, key)
	file_path = f"/home/Host/Project/Registrations/{uid}.txt"
	try:
		dat, tim, name, selec, n = "", "", "", "", ""
		with open(file_path, "r") as file:
			for line in file:
				elements = line.split()
				dat = elements[0]
				tim = elements[1]
				name = elements[2]
				selec = elements[3]
				n = elements[4]
		tim = tim[:len(tim)-1]
		print("Purchase Details:\n")
		print(f"Time of Purchase: {dat}, {tim}\nRegistered Name: {name}\nCycle: {selec}")
		if otp == n:
			with open("/home/Host/Project/cycles.txt", "r") as file:
				for line in file:
					elements = line.split()
					name = elements[0]
					avail = elements[1]
					cycles.append(name, avail)
			current = cycles.head
			with open("/home/Host/Project/cycles.txt", "w") as file:
				while current != None:
					if current.name == selec:
						if current.isAvail == False:
							current.isAvail = True
						else:
							print("Cycle Already Returned!")
							exit(0)
					avail = ""
					if current.isAvail == True:
						avail = "Available"
					else:
						avail = "Not_Available"
					file.write(f"{current.name} {avail}\n")
					current = current.next
			print("Cycle Returned Successfully!")
		else:
			print("Invalid Key")
			exit(-2)
	except FileNotFoundError:
		print("Invalid UID")
		exit(1)
