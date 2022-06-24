from django.shortcuts import render

def homePage(request):
    return render(request, 'frontEnd/home.html', {'title': 'Home'})
