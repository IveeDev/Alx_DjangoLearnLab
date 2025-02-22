from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views      # SignupView, register, user_login, user_logout

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Class Base View
    # path('register/', SignupView.as_view(), name='register'), 
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'), 
    
    
    # Function Based Views
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_logout, name="logout"),
    path("", auth_views.TemplateView.as_view(template_name="home.html"), name="home")  # Home page
]

