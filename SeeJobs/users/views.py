from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import UserForm

def RegisterPage(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data.get('password') == form.cleaned_data.get('password2'):
                form.save()
                return redirect('login')
            else:
                return {'errore': 'Password is not correct'}
    else:
        form = UserForm()

    data = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'users/reg.html', data)
def Profile(request):
    return render(request, 'users/profile.html')