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

# Seed some data (via internal route)
def seed(request):
  Character.objects.create(name='Jeff Winger', mood='Obnoxious', quote='I am awesome')
  Character.objects.create(name='Brita Perry', mood='Frustrated', quote='I lived in NY')
  Character.objects.create(name='Abed Nadir', mood='Weird', quote='Cool cool cool')
  return HttpResponse('done')

def characters_detail(request, character_id):
  print('incoming character wildcard value is', character_id)
  character = Character.objects.get(id= character_id)
  return render(request,'characters/detail.html', {'character': character})
  


