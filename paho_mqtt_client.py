import paho.mqtt.client as mqtt # Import the MQTT library
import time # The time library is useful for delays
import subprocess as sub
import socket
import os
import ConfigParser

# Config reading and valuable init
config = ConfigParser.RawConfigParser()
scriptDir = os.path.dirname(os.path.realpath(__file__))
config.read('config.ini')

brokerAddress = config.get('connection', 'broker_address')
brokerPort = config.get('connection', 'broker_port')


# "on message" event
def messageFunction (client, userdata, message):
    hostname = socket.gethostname()
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic +' '+ message)
    if topic == "ls/"+str(hostname):
        r = sub.Popen(['ls','-lha'])
    elif topic == "df/"+str(hostname):
        r = sub.Popen(['df','-h'])
    elif topic == "date/"+str(hostname):
        r = sub.Popen(['date'])
    elif topic == "touch/"+str(hostname):
        r = sub.Popen(['touch', str(hostname)])
    elif topic == "reboot/"+str(hostname):
        r = sub.Popen(['systemctl','reboot'])


print("Starting client...")
print("#####################")
hostname = socket.gethostname()
client = mqtt.Client(hostname) 
client.connect(brokerAddress, brokerPort)
client.subscribe([("reboot/"+str(hostname),1),("touch/"+str(hostname),1),("date/"+str(hostname),1),("df/"+str(hostname),1),("ls/"+str(hostname),1)]) # QoS 0 = At most once, 1 = At least once , 2 = Exactly once
client.on_message = messageFunction
client.loop_start()

# Main program loop
while(1):
    print("Listening...")
    time.sleep(1) # Sleep for a second