from django.conf.urls import include, url

from . import views

app_name = 'music'
urlpatterns = [
    # ex: /music/
    url(r'^$', views.OutfitIndexView.as_view(), name='outfits'),
    # ex: /music/nickpale/...
    url(r'^(?P<slug>[\w-]+)/', include([
        # ex: /music/nickpale/
        url(r'^$', views.OutfitView.as_view(), name='outfit'),
        # ex: music/nickpale/electricdirt...
        url(r'^(?P<slug>[\w-]+)/', include([
            # ex: music/nickpale/electricdirt/
            url(r'^$', views.AlbumView.as_view(), name='album'),
            # ex: music/nickpale/electricdirt/closingin
            url(r'^(?P<slug>[\w-]+)/$', views.TrackView.as_view(), name='track')
        ]))
    ]))
]
