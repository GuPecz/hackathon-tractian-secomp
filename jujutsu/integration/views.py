from django.shortcuts import render
from .models import FichaTecnica
from django.http import JsonResponse, HttpResponse
import json
from .gpt_api import gpt_api

def call_api(nome, tipo, fabricante, img1, img2, img3):
    data = {
        "name": nome,
        "manufacturer": fabricante,
        "model": tipo,
    }
    json_data = json.dumps(data)
    json_output = gpt_api(json_data, img1, img2, img3)
    return json.loads(json_output)

def register(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        fabricante = request.POST.get('fabricante')
        tipo = request.POST.get('tipo')
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