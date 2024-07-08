from openai import OpenAI
client = OpenAI()
 
assistant = client.beta.assistants.create(
  instructions=
  """
  
    You will be provided with customer service queries.
    Your task is to respond to these queries in a helpful and informative manner.
    You must answer these queries only from the pdf provided and nowhere else.
    If a question irrelevant to the pdf's information is asked, politely reject the customer and prompt them to ask something relevant.
    
  """,
  model="gpt-4o",
  tools=[{"type": "file_search"}]
)

vector_store = client.beta.vector_stores.create(name="Document Data")
 

file_paths = ["pfs.pdf"]
file_streams = [open(path, "rb") for path in file_paths]
 

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id=vector_store.id, files=file_streams
)
 

print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
  assistant_id=assistant.id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

print(assistant.id)