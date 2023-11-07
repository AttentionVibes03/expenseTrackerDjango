from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def SignUp(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            #messages.success(request, ('Registration Successfull'))
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'users/signup.html', {'form':form})    
