# Sandbox Anthropic

A sandbox project for experimenting with the Anthropic API.

## Setup

1. Clone the repository
2. Create a `.env` file with your Anthropic API key:
```
ANTHROPIC_API_KEY=your-api-key
```

3. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate sandbox-anthropic
```

## Dependencies

- Python 3.11
- anthropic
- python-dotenv

## Usage

To use the Anthropic API:

```python
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Client()
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT
