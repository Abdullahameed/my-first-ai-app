import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

history=["system started"]

print("AI Assistant Started")

while True:

    user=input("\nYou: ")

    if user.lower()=="exit":
        break

    history.append("User: "+user)

    full_prompt="\n".join(history)

    response=model.generate_content(
        full_prompt
    )

    ai=response.text

    history.append(
        "AI: "+ai
    )

    print("\nAI:", ai)