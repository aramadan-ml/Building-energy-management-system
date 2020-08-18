import time
import paho.mqtt.client as mqtt
   

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/#")

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8") 
 
    #HVAC
    if msg.topic == "current value":
        if msg.payload == "1":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "current value":
        if msg.payload == "0":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    #heater
    if msg.topic == "heater":
        if msg.payload == "1":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "heater":
        if msg.payload == "0":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    #pumps
    if msg.topic == "pumps":
        if msg.payload == "1":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "pumps":
        if msg.payload == "0":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    #light
    if msg.topic == "light":
        if msg.payload == "1":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "light":
        if msg.payload == "0":
            print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))

    #Print humidity and temperature values
    if msg.topic == "current value":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "air conditioner":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "current value":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "heater":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "pumps":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "pumps":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "light":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    if msg.topic == "light":
        print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
 

client=mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)


client.loop_forever()
client.disconnect()
time.sleep(30)