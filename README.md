# MobilityPlatform
This is the model for a `Tech-Based Mobility Platform`, made as a part of the project - `Cyber Attacks on Autonomous Robotic Systems` i.e., we need to analyse the effects of various cyber attacks on this system made on [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) and make improvements (if possible)
# File Management
The files for the client server are all stored in `main/Client` and that for the hosy server is contained in `main/Host`.<br />
In the Raspberry pi, these files are stored in `~/Project` for both client and host.
# Working of the model
The Client is connected to the host server by using `SSH` protocol.<br />
Firstly, the client server will ask the user to enter their credentials using the `Registration.register()` function in the `[Client_Server.py](Client/Client_Server.py)` file
