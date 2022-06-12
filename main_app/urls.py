from django.urls import path
from . import views

urlpatterns = [
  # app level home 
  path('',views.home, name='home'),
  path('about/', views.about, name='about'),
  path('characters/',views.index, name='index'),
  path('characters/<int:character_id>/', views.characters_detail, name='detail'),
  
]
