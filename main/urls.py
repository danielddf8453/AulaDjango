from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista')
]

#A url é que está chamando a função