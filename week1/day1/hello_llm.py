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
role = "user"
content = "DO YOU KNOW VIRAT KOHLI?"

message = {
    "role": role,
    "content": content
}
messages = [message]
response = client.chat.completions.create(
    model=model,
    messages=messages
)
print(response)

print("---------------------------------")

answer = response.choices[0].message.content
print(answer)