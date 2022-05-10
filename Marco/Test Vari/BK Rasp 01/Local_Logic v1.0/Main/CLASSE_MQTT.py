import paho.mqtt.client as mqtt
import json
import time


class MQTT_Network():

    def __init__ (self):

        self.client = mqtt.Client()

        #load setup file (JSON fomat)
        setup_file = open("MQTT_SETUP.txt")
        self.setup = json.load(setup_file)
        setup_file.close()

        #Set attributes
        self.BROKER_IP = self.setup["broker_ip"]
        self.topics = {}
        
    # Debug function to print all class attrs
    def Print_Attributes(self):
        print(self.BROKER_IP)
        print(self.topics)

    # Topics subscription method (method for overwriting)
    def topics_subscriptions(self):
        print("No topics loaded")
        self.client.subscribe("test")

    # The callback for broker CONNECTION
    def on_connect(self, client, userdata, flags, rc):
        print( "Connected with result code " + str(rc) )
        self.topics_subscriptions()

    # The callback for SUBSCRIBE
    def on_subscribe(self, client, userdata, mid, granted_qos):
        print('Successfully subscribed!')

    # Function to publish messages on network
    def publish_msg(self, topic, payload):
        dumped_payload = json.dumps(payload, indent=4)
        self.client.publish( topic, dumped_payload, 2)

    # Topics subscription method (method for overwriting)
    def messages_logic(self, topic, payload):
        print("No messages logic loaded")
        print (topic, payload)
        
    # The callback for when a message arrives from the broker.
    def on_message(self, client, userdata, msg):
        print("\nMessage received:")
        payload = msg.payload.decode("utf-8","ignore")
        payload = json.loads(payload)
        self.messages_logic(msg.topic, payload)

    # Client thread start function
    def Start(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        #self.client.on_publish = self.on_publish
        self.client.connect(self.BROKER_IP)
        self.client.loop_start()
        print("\nMQTT network started")

    # Client thread start function
    def Stop(self):
        self.client.loop_stop()
        print("\nMQTT network stopped")
    
    def Loop(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        #self.client.on_publish = self.on_publish
        self.client.connect(self.BROKER_IP)
        print("\nMQTT network started")
        self.client.loop_forever()
