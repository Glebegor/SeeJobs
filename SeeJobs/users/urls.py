from django.urls import path
from . import views as viewsUser
from django.contrib.auth import views as authView

urlpatterns = [
    path('reg/', viewsUser.RegisterPage, name="reg"),
    path('login/', authView.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('exit/', authView.LogoutView.as_view(template_name='users/exit.html'), name="exit"),
    path('profile/', viewsUser.Profile, name='profile')
]