from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('film', views.film, name='film'),
    path('mult', views.mult, name='mult'),
    path('create', views.create, name='create'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
