
from django.shortcuts import render, redirect
from django.contrib import messages

PASSWORD = 'Password123'
USERNAME = 'student'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username != USERNAME:
            messages.error(request, "Your username is invalid!")
        elif password != PASSWORD:
            messages.error(request, "Your password is invalid!")
        else:
            return redirect('success')

    return render(request, 'loginapp/login.html')

def success_view(request):
    return render(request, 'loginapp/success.html')

def logout_view(request):
    return render(request, 'loginapp/logout.html')