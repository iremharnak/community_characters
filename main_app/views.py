from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# import character model
from .models import Character


class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'
  success_url = '/characters/'

class CharacterUpdate(UpdateView):
  model = Character
  fields = '__all__'
  success_url = '/characters/'


class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters/'
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
  



