from dotenv import load_dotenv
load_dotenv()

import anthropic

response = anthropic.Anthropic().messages.count_tokens(
    model="claude-3-5-sonnet-20241022",
    messages=[
        {"role": "user", "content": "Hello, world"},
        {"role": "assistant", "content": "Hey there! How are you?"}
    ]
)
print(response)