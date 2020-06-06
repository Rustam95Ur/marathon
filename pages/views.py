from django.shortcuts import render
from competitions.models import Competition


def home_page(request):
    competitions = Competition.objects.filter(is_active=True).order_by('-id')[:6]
    data = {'competitions': competitions}
    return render(request, 'page/home.html', context=data)
