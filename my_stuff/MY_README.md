# README

## Activate Python Environment

- On Windows: `.\.venv\Scripts\activate`
- On MacOS/Linux `source .venv/bin/activate`

#### Create Virtual Environment

- from the terminal, enter: `python -m venv .venv`   (You might need to install something for this)

Current package needed (may need to be updated. I got this list from setup.py):

- `pip install openai~=1.2 diskcache termcolor flaml python-dotenv tiktoken docker`

## Docker File

I have a setup to run a docker container. Autogen will run on my machine but it will execute
commands in the docker image.

1. Build the docker image (only needed when updated)

```bash
docker build -t autogen-run-image .
```



