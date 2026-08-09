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

def llm_ans(prompt):
    message ={
        "role" : "user",
        "content" : prompt
    }
    messages =[message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans

prompt = """ 
#Role 
you are a professional psychiatrist.you have to handle the mental patients.
#task
classify the problem.what kind of problem it is?
#constrains 
the problem should be in those particular field,"emotional, physical, attachment, distance".
#output format
result should be in one word
#Example 
as if he/ she gets injured then it will be a physical issue.
#fallback
if its unrealed problem returen Other.

i love my mother so much.
i miss him so much!
i don't know i love her or not.


"""


print(llm_ans(prompt))