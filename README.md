# workshop-tractian-secomp

## Funcionamento do Site

O site foi feito com Django e as aplicações usuais de front end (JS, HTML, CSS). O app integration é responsável por todas as consultas e integração com o ChatGPT.

A integração entre front-end e Django é feita através do Java Script, usando a função fetch dentro de funções assíncronas. Isso permite atualizar o HTML da página lendo as informações do JsonResponse gerado dentro do views do Django.

Há um link secundário onde é feita a listagem das máquinas no banco de dados (são salvas e exibidas apenas as informações inseridas pelo usuário).

## Backend

O Backend foi programado com Python. Ademais, utilizamos a API do chatGPT para realizar o reconhecimento de informações chaves dos equipamentos fotografados, retornando via arquivo JSON os seguinte resultados: 

- Ambiente adequado para o equipamento
- Fabricante
- Estado da máquina 
- Nível de uso da máquina 
- Modelo
- Identificação
- RPM (no exemplo de um motor)
- Frequência 
- Potência
- Tensão

## Como rodar
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd jujutsu
python manage.py makemigrations  # se necessário
python manage.py migrate
python manage.py runserver