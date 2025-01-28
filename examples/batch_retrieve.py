from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

response = client.messages.batches.retrieve(
    "msgbatch_01DfcPxLvpCRa337rQHM8Wbp",
)
print(response)
