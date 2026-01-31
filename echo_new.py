#!/usr/bin/env python3
"""
Echo AI Chatbot - A terminal-based AI assistant
A simple, beginner-friendly chatbot that uses real LLM APIs.
"""

import sys
from typing import List, Dict


def get_llm_response(user_message: str, conversation_history: List[Dict[str, str]]) -> str:
    """
    Get a response from the LLM using OpenAI-compatible API.

    This function makes a real API call to an LLM service.
    Supports OpenAI and OpenAI-compatible APIs (like local LLMs).

    Args:
        user_message: The current message from the user
        conversation_history: List of previous messages with roles

    Returns:
        str: The LLM's response
    """
    # ========================================
    # API KEY CONFIGURATION
    # ========================================
    # Try to get API key from environment variable first
    import os
    API_KEY = os.environ.get("OPENAI_API_KEY", "")

    # If not found in environment, you can set it directly here:
    # API_KEY = "sk-..."  # <--- Alternative: paste your API key here

    # ========================================
    # API ENDPOINT CONFIGURATION
    # ========================================
    # Default to OpenAI, but can be changed for compatible APIs
    # For local LLMs (like Ollama), use: "http://localhost:11434/v1/chat/completions"
    API_BASE_URL = "https://api.openai.com/v1/chat/completions"

    # Model name - adjust based on your API provider
    # OpenAI: "gpt-3.5-turbo", "gpt-4", etc.
    # Local LLMs: "llama2", "mistral", etc.
    MODEL_NAME = "gpt-3.5-turbo"

    # Check if API key is provided
    if not API_KEY:
        return "⚠️ No API key found. Please set it to enable real responses."

    try:
        # Import requests for HTTP calls
        import requests
        import json

        # Prepare the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        # Prepare the payload with conversation history
        payload = {
            "model": MODEL_NAME,
            "messages": conversation_history,
            "temperature": 0.7,  # Controls randomness (0.0-2.0)
            "max_tokens": 500    # Maximum tokens in response
        }

        # Make the API call
        response = requests.post(
            API_BASE_URL,
            headers=headers,
            json=payload,
            timeout=30  # 30 second timeout
        )

        # Check for successful response
        response.raise_for_status()

        # Parse the response
        result = response.json()

        # Extract and return the assistant's message
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"Error: API request failed - {str(e)}"
    except (KeyError, IndexError) as e:
        return f"Error: Unexpected API response format - {str(e)}"
    except Exception as e:
        return f"Error: Could not get response from API - {str(e)}"


def display_welcome_message() -> None:
    """Display the welcome message when Echo starts."""
    print("Echo AI 🤖 — type 'exit' to quit")
    print("-" * 40)


def get_user_input() -> str:
    """
    Get and validate user input from the terminal.

    Returns:
        str: The validated user input
    """
    while True:
        try:
            user_input = input("You: ").strip()

            # Check for empty input
            if not user_input:
                print("Please enter a message. Type 'exit' to quit.")
                continue

            return user_input

        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+D or Ctrl+C gracefully
            print("\nGoodbye! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"Error reading input: {e}")
            continue


def update_conversation_history(history: List[Dict[str, str]], 
                               role: str, 
                               content: str) -> None:
    """
    Add a message to the conversation history.

    Args:
        history: The conversation history list
        role: The role of the message sender ('user' or 'assistant')
        content: The message content
    """
    history.append({"role": role, "content": content})


def main() -> None:
    """
    Main function that runs the Echo AI chatbot.
    Handles the conversation loop and user interaction.
    """
    # Display welcome message
    display_welcome_message()

    # Initialize conversation history
    conversation_history: List[Dict[str, str]] = []

    # Main conversation loop
    while True:
        # Get user input
        user_input = get_user_input()

        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye! 👋")
            break

        # Add user message to history
        update_conversation_history(conversation_history, 'user', user_input)

        # Get response from LLM
        try:
            ai_response = get_llm_response(user_input, conversation_history)

            # Display the response
            print(f"Echo: {ai_response}")

            # Add AI response to history
            update_conversation_history(conversation_history, 'assistant', ai_response)

        except Exception as e:
            print(f"Echo: Sorry, I encountered an error: {e}")


if __name__ == "__main__":
    main()
