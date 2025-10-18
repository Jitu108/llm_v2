import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

print("\n\n")

# Check the key
if not openai_api_key:
    raise ValueError("No OPENAI_API_KEY found in environment variables. Please set it in a .env file.")
    #print("No OPENAI_API_KEY found in environment variables. Please set it in a .env file.")

elif not openai_api_key.startswith("sk-proj-"):
    # print("The OPENAI_API_KEY does not appear to be valid. Please check your .env file.")
    raise ValueError("The OPENAI_API_KEY does not appear to be valid. Please check your .env file.")
else:
    # print("OPENAI_API_KEY found and appears valid.")
    pass

def conventional_api_call():
    headers = {"Authorization": f"Bearer {openai_api_key}", "Content-Type": "application/json"}

    payload = {
        "model": "gpt-5-nano",
        "messages": [
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a fun fact"}
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", 
        headers=headers, 
        json=payload)
    response_data = response.json()["choices"][0]["message"]["content"]

    print(response_data)

def openai_sdk_call():
    openai = OpenAI()

    response = openai.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a fun fact"}
        ]
    )

    response_data = response.choices[0].message.content
    print(response_data)

def gemini_sdk_call():
    gemini = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=google_api_key)

    response = gemini.chat.completions.create(
        model="gemini-2.5-pro",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a fun fact"}
        ]
    )

    response_data = response.choices[0].message.content
    print(response_data)

def ollama_sdk_call():
    ollama = OpenAI(base_url="http://localhost:11434/v1", api_key="olla-api-key")

    response = ollama.chat.completions.create(
        # model="llama3.2",
        model="deepseek-r1:1.5b",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a fun fact"}
        ]
    )

    response_data = response.choices[0].message.content
    print(response_data)

# conventional_api_call()
# openai_sdk_call()
# gemini_sdk_call()

ollama_sdk_call()