from openai import OpenAI
client = OpenAI()
 
assistant = client.beta.assistants.create(
  instructions="You are a helpful assistant. You will identify the topic and use the tool to fetch the relative path.",
  model="gpt-4o",
  tools=[
    {
      "type": "function",
      "function": {
        "name": "get_image_paths",
        "description": "Get the relative paths of the image files within a specified folder named after a fruit or vegetable.",
        "parameters": {
          "type": "object",
          "properties": {
            "topic": {
              "type": "string",
              "description": "The name of the fruit or vegetable."
            }
          },
          "required": ["topic"]
        }
      }
    },
  ]
)

print(assistant.id)