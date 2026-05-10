from openai import OpenAI
import os
import base64
from rich.console import Console
from rich.markdown import Markdown

client = OpenAI(
  base_url="http://localhost:11434/v1",
  api_key="Parsing images using OpenAI SDK",
)

image_folder = "images"

if not os.path.isdir(image_folder):
  print(f"Error: Folder '{image_folder}' not found.")
  exit()

# Find .webp and .png files
image_files = [f for f in os.listdir(image_folder)
         if os.path.isfile(os.path.join(image_folder, f)) and
          (f.lower().endswith(".webp") or f.lower().endswith(".png"))]

if not image_files:
  print(f"No .webp or .png files found in '{image_folder}'.")
  exit()

console = Console()

for image_file in image_files:
  image_path = os.path.join(image_folder, image_file)
  print(f"Processing image: {image_path}")

  image_type = "webp" if image_file.lower().endswith(".webp") else "png"

  try:
    with open(image_path, "rb") as img_file:
      base64_image = base64.b64encode(img_file.read()).decode('utf-8')
  except Exception as e:
    print(f"Error reading or encoding image {image_path}: {e}")
    continue

  data_url = f"data:image/{image_type};base64,{base64_image}"

  try:
    response = client.chat.completions.create(
      model="qwen-nothink",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "Describe this image in detail."},
            {
              "type": "image_url",
              "image_url": {"url": data_url},
            },
          ],
        }
      ],
    )
    print(f"Response for {image_file}:")
    markdown_output = Markdown(response.choices[0].message.content)
    console.print(markdown_output)

  except Exception as e:
    print(f"Error calling API for image {image_path}: {e}")
