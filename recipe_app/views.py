from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get("title"),
                author=data.get("author"),
                description=data.get("description"),
                time_required=data.get("time_required"),
                instructions=data.get("instructions"),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "add_recipe_form.html", {"form": form})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data.get("name"),
                bio=data.get("bio"),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "add_author_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next",reverse("homepage")))

    form = LoginForm()
    return render(request, "login_form.html", {"form": form})


def signup_view(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "signup_form.html", {"form": form})
    


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))