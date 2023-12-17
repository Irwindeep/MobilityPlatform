import os
import sys
import paramiko

global reg_updater, reg_time
reg_updater = 0
reg_time = 0
global reg_name, reg_uid
reg_name = ""
reg_uid = ""

class Main_Menu():
    def main_menu(self):
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Choose one of the following operations (Just type the index of the desired operation): ")
        print('''
        1. Register Yourself
        2. Available Bicycles
        3. Exit
        ''')
        choice = int(input("Your Choice: "))
        os.system("clear")
        if choice == 1:
            Registration().register()
        elif choice == 2:
            Bicycles().cycles()
        elif choice == 3:
            os.system("exit")
        else:
            print("Invalid Choice")


class Registration():
    def register(self):
        global reg_updater, reg_name, reg_uid
        print("\n----Tech-Driven Mobility Platform----\n")
        name = input("Enter your name: ")
        uid = input("Enter a UID of yours (Roll No. given by IITJ): ")
        uid = uid.upper()
        print(f"Hello {name}, you have been registered successfully, please proceed to see available bicycles.")
        proceed = input("Do you wish to proceed(y or n): ")
        if proceed == 'y' or proceed == 'Y':
            os.system("clear")
            reg_updater += 1
            reg_name += name
            reg_uid += uid
            Bicycles().cycles()
        else:
            Main_Menu().main_menu()


class Bicycles(Registration):
    def cycles(self):
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Price: Rs.100/hour for each bicycle")
        usr = "Host"
        pas = "Raspberry"
        ip = "192.168.187.197"
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(ip, username=usr, password=pas)
        stdin, stdout, stderr = ssh.exec_command("python3 ~/Project/cycles.py")
        max_cycles = 0
        for line in stdout:
            print(line.strip())
            max_cycles += 1
        ssh.close()
        cycle_choice = int(input("Enter the index of your desired bicycle: "))
        if cycle_choice <= max_cycles:
            if reg_updater == 0:
                print("Register Yourself")
                Registration().register()
            else:
                ssh.connect(ip, username=usr, password=pas)
                stdin, stdout, stderr = ssh.exec_command(f"python3 ~/Project/cycles.py {cycle_choice}")
                elements = []
                for line in stdout:
                    elements.append(line.strip())
                global cyc
                cyc = elements[0]
                ssh.close()
                print(f"Bicycle {cyc} has been chosen, proceed for Payment")
        else:
            print("Invalid Choice")
            exit(1)
        proceed = input("Do you wish to proceed(y or n): ")
        if proceed == 'y' or proceed == 'Y':
            os.system("clear")
            Payment().pay()
        else:
            Main_Menu().main_menu()


class Payment():
    def pay(self):
        global reg_time
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Price: Rs.100/hour for each bicycle")
        time = float(input("Enter the duration (in hours) for which you wish to rent the bicycle: "))
        reg_time += time
        print("Total Rent: Rs.", 100*time)
        print("GST: Rs.", 5*time)
        print("Amount to be paid: Rs.", 105*time)
        proceed = input("Do you wish to proceed(y or n): ")
        if proceed == 'y' or proceed == 'Y':
            os.system("clear")
            Payment().query()
        else:
            Main_Menu().main_menu()

    def query(self):
        print("\n----Tech-Driven Mobility Platform----\n")
        print("Confirm Your Name and UID:")
        print("Name: "+reg_name+"\nUID: "+reg_uid)
        x = input("Press 1 to confirm (Press any other key to change): ")
        if x == '1':
            print("Username and UID has been confirmed, kindly make the required payment: ")
            print("Total Rent: Rs.", 100 * reg_time)
            print("GST: Rs.", 5 * reg_time)
            print("Amount to be paid: Rs.", 105 * reg_time)
            os.system(f"python3 ./query.py {reg_name} {reg_uid} {cyc}")
        else:
            os.system("clear")
            Registration().register()



if __name__=="__main__":
    os.system("clear")
    Main_Menu().main_menu()
