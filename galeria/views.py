from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from galeria.models import fotografia

def index(request):
  fotografias= fotografia.objects.order_by("data_fotografia").filter(publicada = True)
  return render(request, 'galeria/index.html',{'cards' : fotografias})

def imagem(request, foto_id):
    fotogra = get_object_or_404(fotografia, pk=foto_id)

    return render(request, 'galeria/imagem.html', {"fotografia" : fotogra})

def buscar(request):
    fotografias= fotografia.objects.order_by("-data_fotografia").filter(publicada = True)

    if "buscar" in request.GET:
       nome_buscar = request.GET['buscar']
       if nome_buscar :
          fotog = fotografias.filter(nome__icontains= nome_buscar)
    return render(request, 'galeria/buscar.html',{"cards" : fotog})
