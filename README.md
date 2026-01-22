<div align="center">
  <img src="logo.png" alt="sandbox-anthropic" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
  [![Anthropic](https://img.shields.io/badge/Anthropic-API-orange.svg)](https://www.anthropic.com/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **Learn the Anthropic API through practical, runnable examples**

  [Documentation](https://docs.anthropic.com/) · [API Reference](https://docs.anthropic.com/en/api/getting-started)
</div>

## Overview

A hands-on sandbox for exploring the Anthropic API. Each example demonstrates a specific API feature with minimal, focused code you can run immediately.

## Features

- **Basic Chat** - Simple message creation with the Messages API
- **Streaming** - Real-time token-by-token responses
- **Vision** - Multimodal input with images
- **Batch Processing** - Create, list, retrieve, and process batch requests
- **Token Counting** - Calculate usage before API calls
- **Model Info** - Query available models and details

## Quick Start

```bash
# Clone and setup
git clone https://github.com/tsilva/sandbox-anthropic.git
cd sandbox-anthropic
conda env create -f environment.yml
conda activate sandbox-anthropic

# Configure API key
echo "ANTHROPIC_API_KEY=your-api-key" > .env

# Run an example
python examples/streaming.py
```

## Installation

### Using Conda (Recommended)

```bash
conda env create -f environment.yml
conda activate sandbox-anthropic
```

### Using the Activation Script

```bash
source activate-env.sh
```

The script automatically creates the environment if needed and activates it.

### Manual Installation

```bash
pip install anthropic python-dotenv
```

## Usage

### Basic Chat

```python
from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(message.content[0].text)
```

### Streaming Responses

```python
with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Tell me a story"}],
    model="claude-3-5-sonnet-20241022",
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### Vision (Image Input)

```python
import base64
import httpx

image_url = "https://example.com/image.jpg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [{
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": image_data,
            },
        }]
    }],
)
```

### Batch Processing

```python
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

response = client.messages.batches.create(
    requests=[
        Request(
            custom_id="request-1",
            params=MessageCreateParamsNonStreaming(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": "Hello"}]
            )
        )
    ]
)
```

## Examples

| File | Description |
|------|-------------|
| `chat_1.py`, `chat_2.py`, `chat_3.py` | Basic message creation patterns |
| `streaming.py` | Real-time streaming responses |
| `vision.py` | Image analysis with base64 encoding |
| `batch_create.py` | Create batch requests |
| `batch_list.py` | List all batches |
| `batch_retrieve.py` | Get batch status |
| `batch_result.py` | Fetch batch results |
| `count_tokens.py` | Pre-calculate token usage |
| `list_models.py` | Query available models |
| `get_model.py` | Get model details |

Run any example:

```bash
python examples/<filename>.py
```

## Configuration

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your-api-key
```

All examples use `claude-3-5-sonnet-20241022` as the default model.

## Project Structure

```
sandbox-anthropic/
├── examples/
│   ├── chat_*.py          # Basic chat examples
│   ├── streaming.py       # Streaming responses
│   ├── vision.py          # Image input
│   ├── batch_*.py         # Batch processing
│   ├── count_tokens.py    # Token counting
│   └── *_model*.py        # Model info
├── main.py                # Entry point example
├── environment.yml        # Conda environment
├── activate-env.sh        # Environment activation script
└── .env                   # API key (create this)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-example`)
3. Commit your changes (`git commit -m 'Add new example'`)
4. Push to the branch (`git push origin feature/new-example`)
5. Open a Pull Request

## License

MIT
