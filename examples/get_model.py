import anthropic

client = anthropic.Anthropic()

response = client.models.get("claude-3-5-sonnet-20241022")

print(response)
