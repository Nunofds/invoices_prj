from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.conf import settings
from .forms import *
from .models import *

from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4


# starts Anonymous required decorator
def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = 'dashboard'

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)

    return actual_decorator


# ends Anonymous required decorator


def index(request):
    context = {}
    return render(request=request, template_name='invoice/index.html', context=context)


@anonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'invoice/login/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
        else:
            messages.error(request, 'Invalid form data. Please check your input.')
        return redirect('login')

    return render(request, 'invoice/login/login.html', context)


@login_required
def dashboard(request):
    context = {}
    return render(request=request, template_name='invoice/dashboard/dashboard.html', context=context)
