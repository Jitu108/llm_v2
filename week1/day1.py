import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI

# If you get an error here, make sure you have a .env file with your OPENAI_API_KEY

# Load environment variables from .env file
load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

print("\n\n")

# Check the key
if not api_key:
    raise ValueError("No OPENAI_API_KEY found in environment variables. Please set it in a .env file.")
    #print("No OPENAI_API_KEY found in environment variables. Please set it in a .env file.")

elif not api_key.startswith("sk-proj-"):
    # print("The OPENAI_API_KEY does not appear to be valid. Please check your .env file.")
    raise ValueError("The OPENAI_API_KEY does not appear to be valid. Please check your .env file.")
else:
    # print("OPENAI_API_KEY found and appears valid.")
    pass

openai = OpenAI()

# Define our system prompt and user prompt
systemPrompt = """
You are an assistant that analyzes the content of websites,
 and provides a brief summary, ignoring text that might be navigation related. 
 Respond in markdown."""

userPromptPrefix = """
Here are the contents of a website.
Provide a short summary fo this website in markdown format.
If it includes news or announcements, then summarize those as well.
"""

def message_for(website: str) -> list[dict[str, str]]:
    return [
    {"role": "system", "content": systemPrompt},
    {"role": "user", "content": userPromptPrefix + website},
]

def summarize_website(url: str) -> str:
    website = fetch_website_contents(url)

    response = openai.chat.completions.create(
        model="gpt-4.1-nano",
        messages=message_for(website),
    )
    summary = response.choices[0].message.content
    return summary

def display_summary(url: str):
    summary = summarize_website(url)
    print(summary)
    #display(Markdown(f"## Summary of {url}\n\n{summary}"))

display_summary("https://curiticshealth.com")


print("\n\n")
