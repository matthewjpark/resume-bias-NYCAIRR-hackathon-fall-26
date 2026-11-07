import os
from openai import OpenAI
from api_key import get_openai_key

client = OpenAI(
    # This is the default and can be omitted
    api_key=get_openai_key(),
)
response = client.responses.create(
    model="gpt-6-luna",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)