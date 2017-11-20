from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    # CRUD
    url(r'^album/add/$', views.AlbumCreate.as_view(), name="album_add"),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album_update"),
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="album_delete"),

    # Login
    url(r'^register/$', views.UserFormView.as_view(), name="register"),



    # url(r'^$', views.index, name="index"),
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    # url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name="favorite"),
]
