from django.urls import path
from . import views

urlpatterns = [
  # app level home 
  path('',views.home, name='home'),
  path('about/', views.about),
  path('characters/',views.index)
]
