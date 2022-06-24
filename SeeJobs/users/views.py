from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import UserForm

def RegisterPage(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    data = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'users/reg.html', data)