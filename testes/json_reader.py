import json 

data = []
for i in range(1, 31):
    with open(f'labels/assets_data/{i}/asset_info.json') as file:
        informacoes = json.load(file)
        data.append(informacoes)

with open('informacoes.txt', 'w+') as file:
    for info in data[0].keys():
        file.write(info + '\n')
        for i, dict in enumerate(data):
            file.write(str(i + 1) + ' - ' + dict[info] + '\n')
        file.write('\n')

unique_models = []
for i, dict in enumerate(data):
    if dict['model'] not in unique_models:
        unique_models.append(dict['model'])
unique_models.sort()
with open('models.txt', 'w+') as file:
    for i, model in enumerate(unique_models):
        file.write(model + '\n')