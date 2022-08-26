import os
import threading
import time

from slack_sdk import WebClient
from slack_sdk.rtm_v2 import RTMClient

rtm = RTMClient(token=os.environ["SLACK_ADVENTURE_TOKEN"])
client = WebClient(token=os.environ["SLACK_ADVENTURE_TOKEN"])
channels = {}


class Game:
    def __init__(self, channel):
        self.channel = channel
        self.thread = threading.Thread(target=self.run)
        self.condition = threading.Condition()
        self.queue = []

    def start(self):
        self.thread.start()

    def receive(self, message):
        with self.condition:
            self.queue.append(message)
            self.condition.notifyAll()

    def send(self, message):
        client.api_call(
            "chat.postMessage",
            params={"channel": self.channel, "as_user": True, "text": message},
        )

    def response_wait(self, _):
        while True:
            with self.condition:
                if self.queue:
                    return self.queue.pop(0)
                self.condition.wait(1.0)

    def run(self):
        with open("main.py") as fobj:
            data = fobj.read()
        codex = compile(data, "main.py", "exec")  # noqa # nosec
        exec(codex, {"print": self.send, "input": self.response_wait})  # noqa # nosec
        del channels[self.channel]


@rtm.on("message")
def handle(client: RTMClient, event: dict):
    if event.get("bot_id"):
        return
    if event["text"]:
        channel = event["channel"]
        game = channels.get(channel)
        if game is None and event["text"] == "start":
            game = Game(channel)
            channels[channel] = game
            game.start()
        elif game is not None:
            game.receive(event["text"])


rtm.connect()
time.sleep(1 << 30)
