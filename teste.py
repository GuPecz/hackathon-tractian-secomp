from openai import OpenAI
import os
import base64
import requests
import json
import glob


print(os.environ.get('OPENAI_API_KEY'))
client = OpenAI()


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
data_folder = "./10"
#foto_placa = data_folder+"/image1.jpg"
#foto_equipamento = data_folder+"/image2.jpg"
#foto_lugar = data_folder+"/image3.jpg"
info_json = data_folder+"/asset_info.json"
prompt_json = "prompt.json"

def get_first_three_jpg_images(folder_path):
    # Use glob to find all .jpg files in the folder
    jpg_files = glob.glob(os.path.join(folder_path, "*.jpg"))
    
    # Sort the files to ensure consistent order
    jpg_files.sort()
    
    # Get the first three .jpg files
    first_three_jpgs = jpg_files[:3]
    
    return first_three_jpgs


# Get the first three .jpg images
jpg_images = get_first_three_jpg_images(data_folder)

# Assign the images to variables
if len(jpg_images) >= 3:
    foto_placa = jpg_images[0]
    foto_lugar = jpg_images[1]
    foto_equipamento = jpg_images[2]
else:
    print("Not enough .jpg images in the folder.")


# Getting the base64 string
base64_placa = encode_image(foto_placa)
base64_equipamento = encode_image(foto_equipamento)
base64_lugar = encode_image(foto_lugar)

# Read the JSON file
with open(info_json, "r") as json_file:
    data = json.load(json_file)
with open(prompt_json, "r") as json_file:
    prompt = json.load(json_file)

system_prompt = prompt.get("system_prompt")
user_prompt = prompt.get("user_prompt")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": json.dumps(data)},
    {
        "role": "user", "content": [
        {"type": "text", "text": user_prompt[0]},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_placa}",
            "detail": "high",
          },
        },
        {
          "type": "image_url",
          "image_url": {
              "url": f"data:image/jpeg;base64,{base64_equipamento}",
              "detail": "high",
          },
        },
        {
          "type": "image_url",
          "image_url": {
              "url": f"data:image/jpeg;base64,{base64_lugar}",
              "detail": "high",
          },
        }
      ],
    },
  ],  
  max_tokens=300,
)

print(completion.choices[0].message.content)
