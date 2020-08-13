from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipesList.as_view(), name='recipes_list'),
]
