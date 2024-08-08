from openai import OpenAI
import base64
import json

prompt_json = "gpt_prompt.json"

# Function to encode the image on image_path to base64
def encode_image(image_path:str)->str:
  '''
  Codifica uma imagem em base64.

    Args:
        image_path (str): O caminho para a imagem.

    Returns:
        str: A string codificada em base64 da imagem.'''
  image_path = ('..' + image_path)[1:]
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Uses the gpt4-o-mini to obtain the specifications for the images machine
def gpt_api(input_json:str, imagem_lugar:str, imagem_equipamento:str, imagem_placa:str)->str:
    '''
    Interage com a API GPT-4 para gerar uma resposta baseada em um prompt e imagens fornecidas.

    Args:
        input_json (str): Caminho para o JSON de entrada.
        imagem_lugar (str): Caminho para a imagem do lugar.
        imagem_equipamento (str): Caminho para a imagem do equipamento.
        imagem_placa (str): Caminho para a imagem da placa.

    Returns:
        dict: A resposta da API GPT-4 como um objeto JSON.'''
    client = OpenAI()

    # Getting the base64 string
    base64_placa = encode_image(imagem_placa)
    base64_equipamento = encode_image(imagem_equipamento)
    base64_lugar = encode_image(imagem_lugar)

    data = input_json
    with open('integration/' + prompt_json, "r") as json_file:
        prompt = json.load(json_file)

    system_prompt = prompt.get("system_prompt")
    user_prompt = prompt.get("user_prompt")

    #calls the api for completion
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
          {"role": "system", "content": system_prompt},
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
        max_tokens=3000,
    )   
    message = completion.choices[0].message.content
    return message[8:-4]

