from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('list_books_2')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'usermodule/login.html', {'form': form})

   
def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('list_books_2')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = SignUpForm()
    return render(request, "usermodule/register.html", {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login') # to landing page
