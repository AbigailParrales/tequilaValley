from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm    # Default Django form
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if(request.method == 'POST'):
        # form = UserCreationForm(request.POST) # Using Django default form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Yout account has been created, you are now able to log in!')
            # Redirect user to home page
            # return redirect('blog-home')
            return redirect('login')
    else:
        # form = UserCreationForm() # Using Django default form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')