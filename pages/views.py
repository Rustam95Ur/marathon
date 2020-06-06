from django.shortcuts import render
from competitions.models import Competition
from django.http import HttpResponseRedirect
from .models import Page


def home_page(request):
    competitions = Competition.objects.filter(is_active=True).order_by('-id')[:6]
    data = {'competitions': competitions}
    return render(request, 'page/home.html', context=data)


def page_view(request, page_slug):
    page = Page.objects.filter(slug=page_slug).first()
    if page:
        data = {'page': page}
        return render(request, 'page/view.html', context=data)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
