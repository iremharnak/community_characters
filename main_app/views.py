from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# import character model
from .models import Character
from .models import Location
from .models import Episode





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
  
# add episode
def add_episode_method1(request, character_id):
  try:
    # hey database, give me the cat that has id 14
    c = Character.objects.get(id=character_id)
    # get a hold of this cat's feedings
    Episode.objects.create(
      season=request.POST['season'], 
      episode=request.POST['episode'],
      character_id=character_id,
      )
    return redirect(f'/characters/{character_id}')
  except:
    return HttpResponse('something went wrong. probably bad form data')
