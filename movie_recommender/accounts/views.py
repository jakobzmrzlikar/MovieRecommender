from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            user = form.save()
            login(request, user)
            return render(request, 'movies/index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)