# OpenAI Assistants API Quickstart - Python

This repository hosts two quickstart apps for different use cases: Assistant selects the folder containing the images for displaying them and another Assistant that can handle file searching and displaying a graph via a function call.

## Basic request

To send your first API request with the [OpenAI Python SDK](https://github.com/openai/openai-python), make sure you have the right [dependencies installed](https://platform.openai.com/docs/quickstart?context=python) and then run the following code:

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
```

## Setup

1. If you don’t have Python installed, install it [from Python.org](https://www.python.org/downloads/).

2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.

3. Navigate into the project directory:

   ```bash
   $ cd chatbot
   ```

4. Create a new virtual environment:

   - macOS:

     ```bash
     $ python -m venv venv
     $ . venv/bin/activate
     ```

   - Windows:
     ```cmd
     > python -m venv venv
     > .\venv\Scripts\activate
     ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://platform.openai.com/api-keys) to the newly created `.env` file.

8. Run the app:

In any of the folders, run:

```bash
$ flask run
```

You should now be able to access the app from your browser at the following URL: [http://localhost:5000](http://localhost:5000)!

If the code is just a simple Python script (in document_read), you can run it with:

```bash
$ python my_file.py
```

## Guide for Prompts

**For retrieval_and_graph:**
1. A phrase that contains the words "Disk space usages" and a random location such as India, Bangalore etc.
2. Anything related to the contents of the documents within the assets folder.

**For display_images:**
Any phrase that contains the word "apples", "bananas" or "carrots".

**For document_read:**
Anything related to the uploaded user guide.
Eg: 
1. Can you tell me about the monitor life cycle?
2. Retrieve basic information about the switch.
3. After the first time the admin use logs into a fabric manager appliance, the user is required to change the password. What should be the strength of the password?
