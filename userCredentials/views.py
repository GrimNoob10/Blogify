from django.shortcuts import render , redirect
from .forms import CustomUserCreationForm , CustomAuthenticationForm
from django.contrib.auth import login , logout   , authenticate
from django.contrib import messages


def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render( request , 'userCredentials/register.html' , { 'form' : form })

def loginUser(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request , "Invalid username or password")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'userCredentials/login.html', {'form': form})



def logoutUser(request):
    logout(request)
    return redirect('register')