from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'blog/login.html')


# User Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# User Profile
@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})



@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})