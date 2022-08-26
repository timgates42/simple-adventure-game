import logging
import os
import threading
import time

from slack_sdk import WebClient
from slack_sdk.rtm_v2 import RTMClient

logging.basicConfig()

rtm = RTMClient(token=os.environ["SLACK_ADVENTURE_TOKEN"])
client = WebClient(token=os.environ["SLACK_ADVENTURE_TOKEN"])
channels = {}


class QuitException(Exception):
    pass


class Game:
    def __init__(self, channel):
        self.channel = channel
        self.thread = threading.Thread(target=self.run)
        self.condition = threading.Condition()
        self.queue = []
        self.quit = False
        self.restart = False

    def start(self):
        self.thread.start()

    def receive(self, message):
        with self.condition:
            if message == "quit":
                self.quit = True
            elif message == "restart":
                self.quit = True
                self.restart = True
            else:
                self.queue.append(message)
            self.condition.notifyAll()

    def send(self, message):
        if self.quit:
            raise QuitException()
        self.raw_send(message)

    def raw_send(self, message):
        client.api_call(
            "chat.postMessage",
            params={"channel": self.channel, "as_user": True, "text": message},
        )

    def response_wait(self, _):
        while True:
            with self.condition:
                if self.quit:
                    raise QuitException()
                if self.queue:
                    return self.queue.pop(0)
                self.condition.wait(1.0)

    def run(self):
        with open("main.py") as fobj:
            data = fobj.read()
        try:
            codex = compile(data, "main.py", "exec")  # noqa # nosec
            exec(  # noqa # nosec
                codex, {"print": self.send, "input": self.response_wait}
            )
        except QuitException:
            pass
        except Exception:
            logging.exception("end game")
        del channels[self.channel]
        if self.restart:
            launch(self.channel)
        else:
            self.raw_send("Game Over, type start to begin again.")


def launch(channel):
    game = Game(channel)
    channels[channel] = game
    game.start()


@rtm.on("message")
def handle(client: RTMClient, event: dict):
    if event.get("bot_id"):
        return
    if event["text"]:
        channel = event["channel"]
        game = channels.get(channel)
        if game is None and event["text"] == "start":
            launch(channel)
        elif game is not None:
            game.receive(event["text"])


rtm.connect()
time.sleep(1 << 30)
