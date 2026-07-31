from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
def home(request):
    query = request.GET.get("search", "").lower()

    foods = [
        {
            "name": "Margherita Pizza",
            "description": "Fresh mozzarella & basil",
            "price": 299,
            "image": "/media/foods/pizza.jpg",
        },
        {
            "name": "Chicken Burger",
            "description": "Loaded with cheese",
            "price": 199,
            "image": "/media/foods/burger.jpg",
        },
        {
            "name": "Healthy Salad",
            "description": "Low calorie meal",
            "price": 249,
            "image": "/media/foods/salad.jpg",
        },
    ]

    if query:
        foods = [
            food for food in foods
            if query in food["name"].lower()
        ]

    return render(request, "home.html", {
        "foods": foods,
        "query": query,
    })
@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            print("Username:", username)
            print("Password:", password)

            user = authenticate(
                request,
                username=username,
                password=password
            )

            print("Authenticated User:", user)

            if user is not None:

                login(request, user)

                print("Login Successful")

                messages.success(request, "Welcome Back!")

                return redirect("dashboard")

            else:

                print("Authentication Failed")

                messages.error(request, "Invalid Username or Password")

    else:

        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )
@login_required
def profile(request):
    return render(request, "accounts/profile.html")
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("login")