import os

from kafka import KafkaConsumer
from utils import save_location

LOCATION = os.environ["LOCATION"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

# Create the kafka consumer
consumer = KafkaConsumer(LOCATION, bootstrap_servers=[KAFKA_SERVER])

while True:
    for message in consumer:
        location_data = message.value.decode('utf-8')
        
        save_location(location_data)
