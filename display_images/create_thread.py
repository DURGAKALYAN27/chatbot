from openai import OpenAI
import json
import os

client = OpenAI()

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="What is the content of Apples?",
)

print(thread.id)