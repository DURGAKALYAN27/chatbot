from openai import OpenAI
import json

client = OpenAI()

def get_image_paths(topic: str) -> str:
  return "longpath"

def make_diskSpaceUsage_graph(loc: str) -> str:
  return "43%"

query = input("user >> ")

message = client.beta.threads.messages.create(
  thread_id="thread_JulIHwuLwtEn96WaiVGJCiug",
  role="user",
  content=query,
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
          
        if tool.function.name == "make_diskSpaceUsage_graph":
          data = json.loads(tool.function.arguments)
          location = data["location"]
          output = make_diskSpaceUsage_graph(location)
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
        
    @override
    def on_message_done(self, message) -> None:
        print("assistant >> " + message.content[0].text.value)
 
 
with client.beta.threads.runs.stream(
  thread_id="thread_JulIHwuLwtEn96WaiVGJCiug",
  assistant_id="asst_jGu12NJE0NvmlfBLLew7GhPw",
  event_handler=EventHandler()
) as stream:
  stream.until_done()