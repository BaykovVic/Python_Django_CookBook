from django.shortcuts import render


# Create your views here.


def base_view(request):
    return render(request, 'basepage/base.html')


def carusel_view(request):
    slides = [1, 2, 3]

    context_dict = {'slides': slides}

    return render(
        request, 'basepage/carusel.html',
        context=context_dict
        )
