# MobilityPlatform
This is the model for a `Tech-Based Mobility Platform`, made as a part of the project - `Cyber Attacks on Autonomous Robotic Systems` i.e., we need to analyse the effects of various cyber attacks on this system made on [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) and make improvements (if possible).<br />
The model will generate a key (that can be any service, a bicycle-stand key in case of this model) on the success of payment by the client.
# File Management
The files for the client server are all stored in `main/Client` and that for the hosy server is contained in `main/Host`.<br />
In the Raspberry pi, these files are stored in `~/Project` for both client and host.
# Working of the model
The Client is connected to the host server by using `SSH` protocol.<br />
Firstly, the client server will ask the user to enter their credentials using the `Registration.register()` function in the [Client_Server.py](Client/Client_Server.py) file.<br />
i.e.,<br />
Then, it will call the function `Bicycles.cycles()` and display all the bicycles that are available in the host server using a `SSH` connection made using [paramiko](https://www.paramiko.org/).<br />
After the bicycle is chosen, the function `Payment.pay()` is called and it would after confirming the credentials, call the `Payment().query()` function.<br />
In the `query()` function, another python file would be called i.e., [query.py](Client/query.py) using the following line:<br />
```
os.system(f"python3 ./query.py {reg_name} {reg_uid} {cyc}")
```
Note that variables `reg_name`, `reg_uid` and `cyc` are shared as command-line arguments for the [query.py](Client/query.py) file to access the username, UID and selected cycle model easily.<br />
The [query.py](Client/query.py) file will access the host server to share user credentials using the same `SSH` protocol as before.<br />
The Credentials are shared as below:
```
key = Fernet.generate_key()
cipher = Fernet(key)
name = cipher.encrypt(reg_name.encode())
uid = cipher.encrypt(reg_uid.encode())
selection = cipher.encrypt(cyc.encode())
        
name = base64.urlsafe_b64encode(name).decode()
uid = base64.urlsafe_b64encode(uid).decode()
selection = base64.urlsafe_b64encode(selection).decode()
        
key_str = base64.urlsafe_b64encode(key).decode()
```
i.e, firstly, all the credentials are encrypted using `Fernet(key)` method, and then, since the credentials are now 32 URL-safe base64-encoded bytes, we are required to convert them to strings and that is done using `base64.urlsafe_b64encode(data).decode()` method.<br />
Finally, these credentials are shared to the host server using the following code:
```
stdin, stdout, stderr = ssh.exec_command(f"python3 ~/Project/Host.py {name} {uid} {selection} {key_str}")
```
i.e., the credentials alongwith the key are shared as command-line arguments to the host server.<br />
In the [Host.py](Host/Host.py) file, the credentials will firstly be converted to 32 URL-safe base64-encoded bytes and then the user will be registered as `./Registrations/uid.txt` and the details of the purchase will be updated in that file.<br />
After the user details are updated, the purchased bicycle is flagged as Not_Available using the linked-list made in the [cycles.py](Host/cycles.py) file and the [cycles.txt](/Host/cycles.txt) file is updated. <br />
Finally, a random key (i.e., any service) will be generated and provided to the user.
