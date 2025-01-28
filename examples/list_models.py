from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

response = client.models.list(limit=20)

print(response)
