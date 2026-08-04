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
prompt1 = "hi"
prompt2 = "Explain time travel in detail under 100 words "
prompt3 = "Write a eassay of 1000 word on machine learning!"

prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
    "role": role,
    "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens = 500
    )
    usage = response.usage 
    print(f"prompt: {prompt} --> your_tokes: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} Total_tokens: {usage.
     total_tokens} Finish Reason :{response.choices[0].finish_reason} ")


# prompt = "DO YOU KNOW VIRAT KOHLI?"

# message = {
#     "role": role,
#     "content": prompt
# }
# messages = [message]
# response = client.chat.completions.create(
#     model=model,
#     messages=messages
# )
# print(response)

# print("---------------------------------")

# answer = response.choices[0].message.content
# print(answer)