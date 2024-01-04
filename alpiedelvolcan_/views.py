from django.shortcuts import render

#vista para mostrar la pagina principal
def index(request):
    return render(request, 'base.html')