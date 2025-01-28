from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-3-5-sonnet-20241022",
) as stream:
  for text in stream.text_stream:
      print(text, end="", flush=True)
