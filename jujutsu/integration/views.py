from django.shortcuts import redirect, render
from django.urls import reverse
from .models import FichaTecnica
from django.http import JsonResponse, HttpResponse
import os, sys, json

# module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
# if module_path not in sys.path:
#     sys.path.append(module_path)
from .gpt_api import gpt_api

def call_api(nome, tipo, fabricante, img1, img2, img3):
    data = {
        "name": nome,
        "manufacturer": fabricante,
        "model": tipo,
    }
    json_data = json.dumps(data)
    json_output = gpt_api(json_data, img1, img2, img3)
    print('------------------------------------')
    print(json_output)
    return json.loads(json_output)

# Create your views here.
def register(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        fabricante = request.POST.get('fabricante')
        tipo = request.POST.get('tipo')
        
        # Read uploaded images
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        maquina = FichaTecnica(
            nome=nome,
            tipo=tipo,
            fabricante=fabricante,
            img1=img1,
            img2=img2,
            img3=img3,
        )
        maquina.save()
        json_output = call_api(
            nome, tipo, fabricante,
            maquina.img1.url, maquina.img2.url, maquina.img3.url
        )
        return JsonResponse(json_output)
    return HttpResponse(status=401)

def listagem(request):
    fichas = list(FichaTecnica.objects.all())
    return render(request, 'listagem.html', {'fichas': fichas})

def export_csv(request):
    fichas = list(FichaTecnica.objects.all())
    with open('fichas_tecnicas.csv', 'w+') as file:
        file.write('nome,tipo,fabricante')
        for ficha in fichas:
            nome = ficha.nome
            tipo = ficha.tipo
            fabricante = ficha.fabricante
            file.write(f'{nome},{tipo},{fabricante}\n')
            print(f'{nome},{tipo},{fabricante}\n')
    return redirect(reverse('integration:listagem'))