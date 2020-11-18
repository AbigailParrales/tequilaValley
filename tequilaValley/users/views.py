from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm    # Default Django form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms import UserRegisterForm



# Create your views here.
def register(request):
    if(request.method == 'POST'):
        # form = UserCreationForm(request.POST) # Using Django default form
        form = UserRegisterForm(request.POST)
        
        # Parse email
        mail = form.data.get('email')
        domain = mail.split('@')[1].split('.')[0]

        if form.is_valid() and domain == "itesm":
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Yout account has been created, you are now able to log in!')
            # Redirect user to home page
            # return redirect('blog-home')
            # send_mail(
            #     'Tequila Valley Register',
            #     'Thanks for being part of our community',
            #     'danielaparrales@hotmail.com',
            #     ['danielaparralesd.m@gmail.com'],
            #     fail_silently=False,
            # )
            return redirect('login')
    else:
        # form = UserCreationForm() # Using Django default form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')