# Copyright 2024 TsumiNa.
# SPDX-License-Identifier: MIT


import os

import trafilatura
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from secretary.llm import _get_summary

app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command("/summarize")
def summarize(ack, respond, command, body, logger):
    ack()
    url = command["text"]
    logger.info(f"fetching {url}")
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    logger.info(f"Summarizing {url}")
    msg = _get_summary(text)
    logger.info(body)
    respond(f"URL: {url}\n\n{msg}")


def main():
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
