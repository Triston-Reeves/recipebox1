from django.shortcuts import render
from recipe_app.models import Recipe, Author

def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes})


def recipe_details(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_details.html", {"recipe": my_recipe})


def author_details(request, author_id):
    my_recipe = Recipe.objects.filter(author=author_id)
    my_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_details.html", {"author": my_author, "recipes": my_recipe})

