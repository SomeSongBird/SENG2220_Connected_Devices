import json
import serial as ps
import paho.mqtt.publish as mqtt

# some global variables mainly for the mqtt stuff
BROKER_HOST = "10.43.1.103"                                                                       # (2)
BROKER_PORT = 1883
TOPIC = "ferchrj/pi/python/temperatures"

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
    #mqtt.single(topic=TOPIC,payload=tojson,qos=2,retain=False,hostname=BROKER_HOST,port=BROKER_PORT,auth=None)
"""
    Repeatedly listens for temperature readings from the Arduino.
    Prints out the temperature reading from the Arduino to the command line.
    Saves the temperature reading in a local text file.  Name is temps.txt.  Use Python file operations like the open and write commands.  
    The file should be a list of each temp reading received in comma separate value (csv) format.  In each line add identifying name/value pair data such as: sensor:arduino, temp:64.5 
    (Every time you open a file and write a new line of data to it, make sure you close the file.)
    Publish the received temperature reading to the lab MQTT Event Broker in JSON format.  Format the JSON as such:   { sensor:arduino, temperature:64.5 }
"""