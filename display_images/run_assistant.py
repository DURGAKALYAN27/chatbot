from openai import OpenAI
from icecream import ic
import json
import os

client = OpenAI()

def get_image_paths(topic):
  images_dict = {}
  main_folder = "C:\\coding\\PYTHON_FILES\\functioncalling\\openai-quickstart-python\\examples\\chat-basic\\images"
  topic_folder = os.path.join(main_folder, topic)
  images = os.listdir(topic_folder)
  image_paths = [os.path.join(topic_folder, img) for img in images]
  images_dict[topic] = image_paths
  ic(images_dict)
  return str(images_dict)

message = client.beta.threads.messages.create(
  thread_id="thread_prjAvlow4hznzcLCzRQqGaHq",
  role="user",
  content="What is the content of Apples?",
)

from typing_extensions import override
from openai import AssistantEventHandler
 
class EventHandler(AssistantEventHandler):
    @override
    def on_event(self, event):
      if event.event == 'thread.run.requires_action':
        run_id = event.data.id  
        self.handle_requires_action(event.data, run_id)
 
    def handle_requires_action(self, data, run_id):
      tool_outputs = []
        
      for tool in data.required_action.submit_tool_outputs.tool_calls:
        if tool.function.name == "get_image_paths":
          data = json.loads(tool.function.arguments)
          topic = data["topic"]
          output = get_image_paths(topic)
          tool_outputs.append({"tool_call_id": tool.id, "output": output})
        
      self.submit_tool_outputs(tool_outputs, run_id)
 
    def submit_tool_outputs(self, tool_outputs, run_id):
      with client.beta.threads.runs.submit_tool_outputs_stream(
        thread_id=self.current_run.thread_id,
        run_id=self.current_run.id,
        tool_outputs=tool_outputs,
        event_handler=EventHandler(),
      ) as stream:
        for text in stream.text_deltas:
          print(text, end="", flush=True)
        print()
 
 
with client.beta.threads.runs.stream(
  thread_id="thread_prjAvlow4hznzcLCzRQqGaHq",
  assistant_id="asst_U9wcUQhobzib54daTlYsuQD7",
  event_handler=EventHandler()
) as stream:
  stream.until_done()