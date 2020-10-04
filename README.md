# MQTT, Mosquitto (Broker) and Paho (Client)

##### OS: Ubuntu 18.04
##### NOTE: It works perfectly using the client in a Raspberry Pi (Raspbian OS)
\
Install Mosquitto (MQTT Boker):
```sh
$ sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
$ sudo apt update
$ sudo apt install mosquitto mosquitto-clients
$ sudo systemctl enable mosquitto
$ sudo systemctl status mosquitto (Check the status)
$ mosquitto -v
```
##### NOTE: You have to open TCP port 1883 
\
Install Paho (MQTT Client):
```sh
$ sudo apt update
$ sudo apt install python-pip
$ pip --version
$ sudo pip install paho-mqtt
```
Open the terminal and run the "MQTT Client" with the next command:
```sh
$ python paho_mqtt_client.py
```
After to run the command above, you're going to see:
```sh
#####################
Starting client...
#####################
Listening...
Listening...
```
And to send a message from the MQTT-Broker to the Client, run one of the next command:
```sh
$ mosquitto_pub -h 127.0.0.1 -t "ls/YOUR_HOSTNAME" -m "ls local"
$ mosquitto_pub -h 127.0.0.1 -t "df/YOUR_HOSTNAME" -m "df local"
$ mosquitto_pub -h 127.0.0.1 -t "date/YOUR_HOSTNAME" -m "date local"
$ mosquitto_pub -h 127.0.0.1 -t "reboot/YOUR_HOSTNAME" -m "reboot local" (If you run this command the computer / device is going to be rebooted)
```
##### NOTE: To find out your hostname run the command "hostname"
