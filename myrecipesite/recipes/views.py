from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from recipes.models import Recipe

class RecipesList(ListView):
    model = Recipe
    context_object_name = "recipes"

    # **kwargs = can take any number of keyword arguments, without needing to specify them
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
