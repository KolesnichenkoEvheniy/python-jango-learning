from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    template_name = 'music/detail.html'
    model = Album


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'image']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'image']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned & normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('music:index')

        return render(request, self.template_name, {'form': form})

# def index(request):
#     albums = Album.objects.all()
#     context = {'albums': albums}
#     return render(request, 'music/index.html', context)
#
#
# def detail(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     return render(request, 'music/detail.html', {'album': album})
#
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     try:
#         song = album.song_set.get(id=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': 'No way.'
#         })
#     else:
#         song.is_favorite = not song.is_favorite
#         song.save()
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
