import os,sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

args = sys.argv
if len(args) <2:
    print("No prompt given!!")
    sys.exit(1)

prompt = sys.argv[1]
if "--verbose" in args:
    print(f"User prompt: {prompt}")

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user",parts=[types.Part(text=prompt)])
]

res = client.models.generate_content(model="gemini-2.0-flash-001",contents=messages)

if "--verbose" in args:
    print("GEMINI RESPONSE:\n",res.text)
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
