# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a sandbox project for experimenting with the Anthropic API. It contains example scripts demonstrating various API features including basic chat, streaming, vision, batch processing, and token counting.

## Environment Setup

The project uses Conda for environment management:

```bash
# Create and activate the environment
conda env create -f environment.yml
conda activate sandbox-anthropic

# Or use the activation script
source activate-env.sh
```

The `activate-env.sh` script automatically:
- Detects if the environment exists (creates it if needed)
- Activates the `sandbox-anthropic` environment
- Must be sourced (not executed directly)

## API Configuration

All scripts require a `.env` file with:
```
ANTHROPIC_API_KEY=your-api-key
```

Every script follows the pattern:
```python
from dotenv import load_dotenv
load_dotenv()
import anthropic
client = anthropic.Anthropic()
```

## Running Examples

Execute any example script from the project root:
```bash
python examples/chat_1.py
python examples/streaming.py
python examples/vision.py
python main.py
```

### Key Example Categories

**Basic Chat**: `chat_1.py`, `chat_2.py`, `chat_3.py`, `main.py`
- Simple message creation with the Messages API

**Streaming**: `streaming.py`
- Uses `client.messages.stream()` context manager
- Iterates over `stream.text_stream` for real-time output

**Vision**: `vision.py`
- Demonstrates multimodal input with base64-encoded images
- Downloads image via httpx, encodes to base64, sends in message content

**Batch Processing**: `batch_create.py`, `batch_list.py`, `batch_retrieve.py`, `batch_result.py`
- Create batches with multiple requests using `Request` and `MessageCreateParamsNonStreaming`
- Each request has a `custom_id` for tracking
- List, retrieve, and get results from batch operations

**Model Information**: `list_models.py`, `get_model.py`
- Query available models and model details

**Token Counting**: `count_tokens.py`
- Calculate token usage before making API calls

## Model Usage

All examples use `claude-3-5-sonnet-20241022` as the default model. The model parameter is specified in every `messages.create()` call.

## README Maintenance

The README.md must be kept up to date with any significant project changes.
