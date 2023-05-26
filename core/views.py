from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy

#local imports
from item.models import Category, Item
from .forms import SignupForm, LoginForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:20]
    categories = Category.objects.all()
    return render(request, 'core/index.html',
        {'categories': categories,
        'items': items}
    )

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse_lazy('core:home')

def logout_user(request):
    logout(request)
    return redirect('core:login')
