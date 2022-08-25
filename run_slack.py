import os
import threading
from slack_sdk.rtm_v2 import RTMClient
from slack_sdk import WebClient

rtm = RTMClient(token=os.environ["SLACK_ADVENTURE_TOKEN"])
client = WebClient(token=os.environ["SLACK_ADVENTURE_TOKEN"])
channel = os.environ["SLACK_ADVENTURE_CHANNEL"]
queue = []
condition = threading.Condition()


@rtm.on("message")
def handle(client: RTMClient, event: dict):
    if event.get("bot_id"):
        return
    if event["text"]:
        print(f"Got {event['text']}")
        with condition:
            queue.append(event["text"])
            condition.notifyAll()


def send(msg):
    client.api_call(
        "chat.postMessage", params={"channel": channel, "as_user": True, "text": msg}
    )


def receive(msg):
    while True:
        with condition:
            if queue:
                return queue.pop(0)
            condition.wait(1.0)

rtm.connect()
print("connected...")

with open("main.py") as fobj:
    data = fobj.read()

codex = compile(data, "main.py", "exec")
exec(codex, {"print": send, "input": receive})
