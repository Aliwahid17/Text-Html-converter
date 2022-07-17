from django.urls import path
from texteditor import views

urlpatterns = [
    path('', views.index, name='index')
]