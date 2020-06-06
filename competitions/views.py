from django.shortcuts import render
from .models import Competition
from photos.models import Photo
from django.http import HttpResponseRedirect
from django.http import JsonResponse


def competitions_list(request):
    competitions = Competition.objects.filter(is_active=True)
    data = {'competitions': competitions}
    return render(request, 'competition/list.html', context=data)


def competition_view(request, competition_id):
    competition = Competition.objects.filter(id=competition_id, is_active=True).first()
    if competition:
        data = {'competition': competition}
        return render(request, 'competition/view.html', context=data)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def competition_search(request, competition_id, user_val):
    photos = Photo.objects.filter(runner__user_val__icontains=user_val, competition__id=competition_id).values()
    if photos:
        return JsonResponse({'photos': list(photos)})
    else:
        return JsonResponse({'status': 'not_found'})
