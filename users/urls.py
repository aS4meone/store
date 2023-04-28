from django.urls import path
from users.views import register, login, profile

app_name = 'users'

urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]