from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

client = OpenAI(
  base_url="http://localhost:11434/v1",
  api_key="ollama using OpenAI SDK",
)

response = client.chat.completions.create(
  model="qwen-nothink",
  messages=[
    {
      "role": "system",
      "content": "You are a helpful and friendly assistant."
    },
    {
      "role": "user",
      "content": "What is the meaning of Tokenizer in LLM?"
    }
  ],
  temperature=0.7,
)

console = Console()
markdown_output = Markdown(response.choices[0].message.content)

console.print(markdown_output)