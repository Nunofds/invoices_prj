from django.shortcuts import render


def invoices(request):
    context = {}
    return render(request=request, template_name='invoice/index.html', context=context)
