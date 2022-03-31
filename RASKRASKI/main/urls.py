from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='raskraski'),
    path('about-us', views.about, name='o_raskraskah'),
    path('create', views.create, name='create'),
]
