<div align="center">
  <img src="logo.png" alt="sandbox-anthropic" width="512"/>

  **🧠 Sandbox for experimenting with the Anthropic API 🧪**

</div>

## Overview

A collection of example scripts demonstrating various Anthropic API features including basic chat, streaming, vision, batch processing, and token counting.

## Features

- **Basic Chat** - Simple message creation with the Messages API
- **Streaming** - Real-time response streaming
- **Vision** - Multimodal input with images
- **Batch Processing** - Create and manage batch requests
- **Token Counting** - Calculate usage before API calls

## Quick Start

```bash
# Clone and setup
git clone https://github.com/tsilva/sandbox-anthropic.git
cd sandbox-anthropic

# Create environment
conda env create -f environment.yml
conda activate sandbox-anthropic

# Configure API key
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY

# Run an example
python examples/chat_1.py
```

## Examples

| Script | Description |
|--------|-------------|
| `chat_1.py`, `chat_2.py`, `chat_3.py` | Basic chat interactions |
| `streaming.py` | Real-time response streaming |
| `vision.py` | Image analysis with base64 encoding |
| `batch_create.py` | Create batch requests |
| `batch_list.py` | List batch operations |
| `batch_retrieve.py` | Retrieve batch details |
| `batch_result.py` | Get batch results |
| `count_tokens.py` | Token counting |
| `list_models.py`, `get_model.py` | Model information |

## Requirements

- Python 3.x
- Conda
- Anthropic API key

## License

MIT
