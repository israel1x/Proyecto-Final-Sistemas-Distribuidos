from django.shortcuts import render
from django.http import HttpResponse
from app.Newsapp.models import New

# Create your views here.


def index(request):

    news = New.objects.all()
    noticias = {'noticias',news}
    #return render(request, 'index.html', noticias)
    return HttpResponse("Index News se presenta las noticias top 10")
