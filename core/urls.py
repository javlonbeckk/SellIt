from django.contrib.auth.views import LoginView
from django.urls import path

#local imports
from .views import index, contact, signup, LoginUser, logout_user, about
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

