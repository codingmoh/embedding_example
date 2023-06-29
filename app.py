import chainlit as cl
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY") or "OPENAI_API_KEY"


prompt = f"""You are Mona Lisa the painting and can answer questions about davinci.
You are highly intelligent system that answers user questions."""

def call(query):
    return  openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
    )

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: str):
    result = call(message)
    # send back the final answer
    await cl.Message(content=result['choices'][0]['message']['content']).send()
