import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_gpt(query, model="text-davinci-002"):
    response = openai.Completion.create(
        engine=model,
        prompt=query,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
question = "Qu'est-ce que l'intelligence artificielle ?"
response = chat_gpt(question)
print(response)
