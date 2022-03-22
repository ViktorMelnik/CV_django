from django.shortcuts import render
from .models import Artical


# Create your views here.
def news_home(request):
    news = Artical.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def index(request):
    return render(request, 'index.html')