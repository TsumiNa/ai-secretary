import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import trafilatura
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

downloaded = trafilatura.fetch_url(url)
text = trafilatura.extract(downloaded, config=trafilatura_config)


# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])




template = """
Your task is to execute the instruction given below. The content you will process is delimited by triple single quotes below.
Don't output anything intermediary but only comply to the formatting instructions.
1. Generate a short summary of the content, in max 70 words.
2. Extract the most relevant keywords of the content, at most 10 keywords.
3. {format_instructions}
Content: '''{content}'''
"""

@app.command("/summarize")
def summarize(ack, respond, command):
    ack()
    ... do something ...

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()