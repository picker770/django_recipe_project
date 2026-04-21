from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/detail.html', {'recipe': recipe})


def recipe_create(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'recipes/form.html', {'form': form})


def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'recipes/form.html', {'form': form})


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('home')
    return render(request, 'recipes/delete.html', {'recipe': recipe})