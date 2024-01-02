import openai

# Set your OpenAI GPT-3 API key here
api_key = 'your_api_key'
openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use other engines as well
        prompt=prompt,
        max_tokens=100,  # Adjust as needed
        n=1,
        stop=None,
        temperature=0.7  # Adjust for creativity vs. consistency
    )

    return response.choices[0].text.strip()

# Example usage
user_input = "Tell me a joke."
response = chat_with_gpt(user_input)
print(response)
