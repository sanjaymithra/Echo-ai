# Echo AI Chatbot 🤖

A terminal-based AI chatbot that uses OpenAI's API to provide intelligent responses.

## Features

- Interactive command-line interface
- Real LLM responses using OpenAI API
- Conversation history maintained across messages
- Graceful error handling
- Easy configuration for different API providers

## Prerequisites

- Python 3.6 or higher
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd llm
```

2. Install required packages:
```bash
pip3 install requests
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

Run the chatbot:
```bash
python3 echo_new.py
```

Type your messages and press Enter to get responses. Type `exit` to quit.

## Configuration

You can modify the following settings in `echo_new.py`:

- `API_BASE_URL`: Change to use different API providers
- `MODEL_NAME`: Specify which model to use (e.g., "gpt-3.5-turbo", "gpt-4")
- `temperature`: Controls response randomness (0.0-2.0)
- `max_tokens`: Maximum tokens in the response

## Using Local LLMs

To use local LLMs (like Ollama):

1. Install Ollama: https://ollama.com
2. Modify `echo_new.py`:
   ```python
   API_BASE_URL = "http://localhost:11434/v1/chat/completions"
   MODEL_NAME = "llama2"  # or any model you've downloaded
   ```

## Error Handling

The chatbot handles various error scenarios:
- Missing API key: Shows warning message
- Rate limits: Displays 429 error
- Network issues: Shows connection errors
- Invalid responses: Reports format errors

## License

MIT License - feel free to use and modify as needed!
