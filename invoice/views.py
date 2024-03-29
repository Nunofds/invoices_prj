from django.shortcuts import render


def index(request):
    context = {}
    return render(request=request, template_name='invoice/index.html', context=context)


def login(request):
    context = {}
    return render(request=request, template_name='invoice/login/login.html', context=context)


def dashboard(request):
    context = {}
    return render(request=request, template_name='invoice/dashboard/dashboard.html', context=context)
