from django.shortcuts import render
from .services import get_articles

# Create your views here.


def view_home(request):
    context = {'articles': get_articles()}
    return render(request, 'index.html', context)
