from django.shortcuts import render
#from django.http import HttpResponse
from recipe.models import Recipe

# Create your views here.
def get_index(request):
    title = 'Open Cook'
    recipes = Recipe.objects.all()
    return render(request, 'index.html', locals())

def get_signup(request):
    return render(request, 'signup.html')