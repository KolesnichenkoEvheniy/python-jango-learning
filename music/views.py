from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song


def index(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': 'No way.'
        })
    else:
        song.is_favorite = not song.is_favorite
        song.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
