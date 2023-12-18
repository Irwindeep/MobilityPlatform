import paramiko
from cryptography.fernet import Fernet
import sys
import base64


class SMTH():
    def smth(self):
        x = input("Enter Payment Secret Code: ")
        if x == "PAYMENT_DONE":
            return True
        else:
            return False

reg_name = sys.argv[1]
reg_uid = sys.argv[2]
cyc = sys.argv[3]

trial = 0
while trial < 5:
    y = SMTH().smth()
    if y == True:
        print("Payment Has been made successfully")
        usr = "Host"
        pas = "Raspberry"
        ip = "192.168.187.197"
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(ip, username=usr, password=pas)
        print("Connected to Host Server")
        key = Fernet.generate_key()
        cipher = Fernet(key)
        name = cipher.encrypt(reg_name.encode())
        uid = cipher.encrypt(reg_uid.encode())
        selection = cipher.encrypt(cyc.encode())
        
        name = base64.urlsafe_b64encode(name).decode()
        uid = base64.urlsafe_b64encode(uid).decode()
        selection = base64.urlsafe_b64encode(selection).decode()
        
        key_str = base64.urlsafe_b64encode(key).decode()
        
        print(f"Name: {reg_name}\nUID: {reg_uid}\nSelection: {cyc}")
        stdin, stdout, stderr = ssh.exec_command(f"python3 ~/Project/Host.py {name} {uid} {selection} {key_str}")
        for line in stdout:
            print(line.strip())
        ssh.close()
        break
    else:
        print("Invalid Code, Try again ("+str(4-trial)+" trials left)")
        if trial == 4:
            print("Maximum Number of Attempts Reached")
            break
        trial += 1
else:
    exit(1)
