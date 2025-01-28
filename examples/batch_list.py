from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

response = client.messages.batches.list(
    limit=20
)
print(response)