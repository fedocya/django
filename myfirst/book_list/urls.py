from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    #    path('test/', views.test, name = 'Любое название'),
    #    path('worddjango/', views.worddjango, name = 'Любое название')
]
#