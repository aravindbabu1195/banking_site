from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confpassword = request.POST['password1']
        if password == confpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('cred:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print("User created")

        else:

            messages.info(request, "Password not matching...")
            print("password not matching...")
            return redirect('cred:register')
        return redirect('cred:login')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('bank:home')
