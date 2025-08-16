from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Home (your custom view)
    path('home/', views.home, name='home'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('connections/', views.connections, name='connections'),

]
