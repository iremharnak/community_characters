from django.shortcuts import render
from django.http import HttpResponse
# import character model
from .models import Character


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Define about view
def about(request):
  return render(request, 'about.html')

# Define index view
def index(request):
  # give me a list of characters
  characters = Character.objects.all()
  return render(request, 'characters/index.html', { 'characters': characters})


# show individual character
def characters_detail(request, character_id):
  print('incoming character wildcard value is', character_id)
  character = Character.objects.get(id= character_id)
  return render(request,'characters/detail.html', {'character': character})
  


