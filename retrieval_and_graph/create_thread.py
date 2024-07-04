from openai import OpenAI
client = OpenAI()

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="What is the content of apples?",
)

print(thread.id)