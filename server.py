import json

from redis import StrictRedis


server = StrictRedis(host="localhost", port=6399, password="redis_password", db=0)

# redis ping
print(server.ping())

topic = "example_topic"

data = {
    "name": "alireza",
    "age": 22,
}

print(json.dumps(data))

server.publish(channel=topic, message=json.dumps(data))
