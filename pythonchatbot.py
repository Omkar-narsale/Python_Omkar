from openai import OpenAI
import os

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Welcome to the Python Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye 👋")
            break

        reply = chat_with_gpt(user_input)
        print("ChatBot:", reply)
