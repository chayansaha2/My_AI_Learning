import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("Groq_api_key")

if not my_api_key:
    raise ValueError("api error")

print("API CONNECTED SUCCESSFULLY!")

client = Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""
message_system={
    "role": "system",
    "content": system_prompt
}

role = "user"
text = "Hi my name is chayan and i am 23 years old. i brought a mobile phone from here which is not working now. i am from andhra pradesh. my email is abc@gmail.com. phone number 4587566221 "

prompt = f"""This is a customer ticket.Extract the personal information from this {text}"""

message = {
    "role": role,
    "content": prompt
}
messages = [message_system,message]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format = response_format

)


answer = response.choices[0].message.content
print(answer)

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)