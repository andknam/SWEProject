from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return HttpResponse("This is the page for user profiles.")


def register(request):
    if request.method == 'POST':
        registrationForm = UserRegistrationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save() # This is what saves it to the database
            username = registrationForm.cleaned_data.get('username')
            messages.success(
                request, f'Congratulations {username}, your account has been created.')
            return redirect('klas-home')
    else:
        registrationForm = UserRegistrationForm()
    content = {
        'registrationForm': registrationForm
    }
    return render(request, 'profiles/register.html', content)
