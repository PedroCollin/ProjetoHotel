from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def dan_inn(request):
    return render(request, 'hoteis/dan_inn.html')

def ventania(request):
    return render(request, 'hoteis/ventania.html')

def panela_velha(request):
    return render(request, 'hoteis/panela_velha.html')

def sobre_nos(request):
    return render(request, 'sobre_nos/sobre_nos.html')

def contato(request):
    return render(request, 'contato/contato.html')