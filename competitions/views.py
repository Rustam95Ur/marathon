from django.shortcuts import render
from .models import Competition


def competitions_list(request):
    competitions = Competition.objects.filter(is_active=True)
    data = {'competitions': competitions}
    return render(request, 'competition/list.html', context=data)
