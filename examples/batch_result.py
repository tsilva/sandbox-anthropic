from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

for result in client.messages.batches.results(
    "msgbatch_01DfcPxLvpCRa337rQHM8Wbp",
):
    print(result)