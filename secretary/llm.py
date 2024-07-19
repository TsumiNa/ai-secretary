# Copyright 2024 TsumiNa.
# SPDX-License-Identifier: MIT

import os
from openai import OpenAI


_client = OpenAI()

ASSISTANT_ID = os.environ["ASSISTANT_ID"]


def _get_summary(content: str) -> str:
    thread = _client.beta.threads.create(
        messages=[{"role": "user", "content": f"summarize this content: {content}"}]
    )
    run = _client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID,
        instructions="Please address the user as a scientist. The user has export level knowledge.",
    )
    if run.status == "completed":
        messages = _client.beta.threads.messages.list(thread_id=thread.id)
        msg = messages.data[0]
        print(messages.data[1].content[0].text.value)
    else:
        print(run.status)
    _client.beta.threads.delete(thread.id)
    return msg.content[0].text.value
