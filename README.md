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
```os.system(f"python3 ./query.py {reg_name} {reg_uid} {cyc}")```
Note that variables `reg_name`, `reg_uid` and `cyc` are shared as command-line arguments for the `query.py` file to access the username, UID and selected cycle model easily.<br />
