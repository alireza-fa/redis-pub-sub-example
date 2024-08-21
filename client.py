import json

from redis import StrictRedis


client = StrictRedis(host="localhost", port=6399, password="redis_password", db=0)

topic = "example_topic"

pubsub = client.pubsub()

pubsub.subscribe(topic)

print("waiting for message...")

while True:
    for message in pubsub.listen():
        if message["data"] == 1:
            continue
        match message["type"]:
            case topic:
                # TODO - change serialization. json is not good
                data = json.loads(message["data"])
                print("received message", data["name"], data["age"])
