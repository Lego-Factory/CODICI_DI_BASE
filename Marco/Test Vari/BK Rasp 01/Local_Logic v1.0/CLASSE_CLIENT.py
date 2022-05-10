from CLASSE_MQTT import MQTT_Network
import time

class Client(MQTT_Network):

	def __init__ (self):
		super().__init__()
		self.topics = self.setup["topics"]

	# Topics subscription method 
	def topics_subscriptions(self):
		self.client.subscribe(self.topics["general_topic"])
		self.client.subscribe(self.topics["setup_topic"])
		self.client.subscribe(self.topics["main_topic"])




