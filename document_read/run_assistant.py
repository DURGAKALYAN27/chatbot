from openai import AssistantEventHandler, OpenAI
from typing_extensions import override


client = OpenAI()


thread = client.beta.threads.create()


class EventHandler(AssistantEventHandler):
    @override
    def on_event(self, event):
        if event.event == 'thread.run.requires_action':
            run_id = event.data.id
            self.handle_requires_action(event.data, run_id)
             
    @override
    def on_message_done(self, message) -> None:
        response = message.content[0].text.value
        print("assistant >> " + response)
    
    
while True:
    content = input("user >> ")
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=content
    )
    
    with client.beta.threads.runs.stream(
        thread_id=thread.id,
        assistant_id="asst_IGEfiiifxaXoFUEpyK0kzZQ0",
        event_handler=EventHandler()
    ) as stream:
        stream.until_done()