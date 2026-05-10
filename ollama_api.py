import json

import requests


def generate_response(model_name, prompt_text):
    """
    Generates a response from the Ollama API using the /api/generate endpoint.

    Args:
        model_name (str): The name of the model to use (e.g., "qwen3.5:0:8").
        prompt_text (str): The input prompt for the model.

    Returns:
        dict: The JSON response from the API, or None if an error occurs.
    """
    api_url = "http://localhost:11434/api/generate"
    payload = {"model": model_name, "prompt": prompt_text, "stream": False}

    try:
        # Using the json= parameter automatically handles json.dumps and headers
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error contacting Ollama API: {e}")
        return None


if __name__ == "__main__":
    model = "qwen-nothink"
    prompt = input("Enter your prompt: ")

    result = generate_response(model, prompt)

    if result:
        print("API Response:")
        print(json.dumps(result, indent=2))
        print("\nGenerated Response Text:")
        print(result.get("response", "No response text found."))
