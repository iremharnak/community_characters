from django.shortcuts import render

from django.http import HttpResponse


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Define about view
def about(request):
  return render(request, 'about.html')

# Define index view
def index(request):
  return render(request, 'characters/index.html', { 'characters': characters})
# fake data
class Character:  
  def __init__(self, name, mood, quote):
    self.name = name
    self.mood = mood
    self.quote = quote
    
characters = [
  Character('Jeff Winger', 'Obnoxious', 'I am awesome'),
  Character('Brita Perry', 'Argumentative', 'I lived in NY'),
  Character('Abed Nadir', 'Weird', 'Cool cool cool')
]