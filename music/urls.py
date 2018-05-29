from django.urls import include, path

from . import views


app_name = 'music'
urlpatterns = [
    # ex: /music/
    path('', views.OutfitIndexView.as_view(), name='outfits'),
    # ex: /music/nickpale/...
    path('<slug:outfitslug>/', include([
        # ex: /music/nickpale/
        path('', views.OutfitView.as_view(), name='outfit'),
        # ex: music/nickpale/electricdirt...
        path('<slug:albumslug>/', include([
            # ex: music/nickpale/electricdirt/
            path('', views.AlbumView.as_view(), name='album'),
            # ex: music/nickpale/electricdirt/closingin
            path('<slug:trackslug>/', views.TrackView.as_view(), name='track')
        ]))
    ]))
]
