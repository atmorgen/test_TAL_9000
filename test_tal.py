import logging
from flask import Flask, request
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from config import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)

# instantiate Slack client
slack_client = WebClient(token=SLACK_BOT_TOKEN)
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None


# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    print("hello")
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    print(text)


@app.route("/listening", methods=["GET", "POST"])
def hears():
    print(request.get_json())


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    # slack_client.chat_postMessage(channel="tal_9000_test", text="I'm an app!")
    app.run(port=3000, debug=True)
