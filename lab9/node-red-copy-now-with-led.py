import json
import sys
import signal
import serial as ps
import paho.mqtt.publish as mqttp
import paho.mqtt.client as mqttc

# some global variables mainly for the mqtt stuff
BROKER_HOST = "10.43.1.15"                                                                       # (2)
#BROKER_HOST = "127.0.0.1" #localhost for testing
BROKER_PORT = 1883
CLIENT_ID = "LEDClient"
TOPIC = "ferchrj/pi/python/temperatures"
LEDON = "ferchrj/led/on"
LEDOFF = "ferchrj/led/off"


def main():
    print("To return to the menu, restart the program")
    serial = ps.Serial(port="/dev/ttyS0") #all the default settings are good so I just set the port to read from.

    while True:
        output = serial.read_until() # Read the next line of data from the port
        output = ''.join(map(chr,output)) # byte mapping magic, convers the byte object into a map object holding characters then joining those characters to an empty character
        print("The temperature around the arduino is: "+output[:-2])
        
        formated = {                  #this is all the data that i want to store
            "user":"Chris",
            "sensor":"1",
            "temperature":output[:-2]
            }  
        tojson = json.dumps(formated) #convert the dictionary to an official json string
        
                                    # append it to the end of the temperature csv file
        file = open("temps.txt",'a')
        file.write(tojson[1:-1]+'\n') #when writing, make sure to exclude the {} brackets for formatting sake
        file.close()

        #publish it to the mqtt server broker
        #disabled till the server is on
        mqttp.single(topic=TOPIC,payload=tojson,qos=2,retain=False,hostname=BROKER_HOST,port=BROKER_PORT,auth=None)

"""
MQTT client Related Functions and Callbacks
"""
def on_connect(client, user_data, flags, connection_result_code):
    client.subscribe(LEDON, qos=2)
    client.subscribe(LEDOFF, qos=2)   
    #print("both connected")                                                          # (9)

def on_message(client, userdata, msg):
    """Callback called when a message is received on a subscribed topic."""
    ser = ps.Serial(port="/dev/ttyS0")
    if msg.topic == LEDON:        #O is on, I is off similar to a close or open cirtuit symbol
        ser.write(b"O")
        #print("on")
    elif msg.topic == LEDOFF:
        ser.write(b"I")
        #print("off")


def signal_handler(sig, frame):
    """Capture Control+C and disconnect from Broker."""
    client.disconnect() # Graceful disconnection.
    print("successfully disconnected")
    sys.exit(0)



def init_mqtt():
    global client

    # Our MQTT Client. See PAHO documentation for all configurable options.
    # "clean_session=True" means we don"t want Broker to retain QoS 1 and 2 messages
    # for us when we"re offline. You"ll see the "{"session present": 0}" logged when
    # connected.
    client = mqttc.Client(                                                                      # (15)
        client_id=CLIENT_ID,
        clean_session=False)                                                                    # (16)

    # Setup callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to Broker.
    client.connect(BROKER_HOST, BROKER_PORT)                                                   # (18)



# Initialise Module
init_mqtt()

def ledControl():
    ser = ps.Serial(port="/dev/ttyS0")
    print("To return to the menu, restart the program")
    print("control the LED state by typing [on] or [off]")
    while True:
        command = input()
        if command.lower()=="on":
            ser.write(b'O')
        if command.lower()=="off":
            ser.write(b'I')

def menu():
    while True:
        command = input("Select an option: [1] change the LED state, [2] read temperature\nEnter [q] to quit\n")
        if (command=='1'):
            ledControl()
        if (command=='2'):
            main()
        if (command.lower()=='q'):
            break

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Capture Control + C                        # (19)
    client.loop_start()
    menu()                                                                    # (20)