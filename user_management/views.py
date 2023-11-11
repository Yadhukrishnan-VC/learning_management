from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
UserModel = get_user_model()

@login_required(login_url='login')
def home(request):
    return render(request,'user_management/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered.')
            return redirect('dashboard')  # Redirect to the user dashboard
    else:
        form = UserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        data=request.POST.copy()
        if 'email' in request.POST:
            user = UserModel.objects.filter(email=request.POST.get('email')).first()
            if user:
                data['username']=user.username
            
        form = AuthenticationForm(request, data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to your home page or any other desired page
    else:
        form = AuthenticationForm()
    return render(request, 'user_management/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to the login page

@login_required
def change_password(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed.')
            return redirect('index')  # Redirect to the user dashboard
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_management/profile.html', {'form': form})




