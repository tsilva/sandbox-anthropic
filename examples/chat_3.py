from dotenv import load_dotenv
load_dotenv()

import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1,
    messages=[
        {"role": "user", "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae"},
        {"role": "assistant", "content": "The answer is ("}
    ]
)
print(message)
