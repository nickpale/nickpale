from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Outfit, Album, Track


class OutfitIndexView(generic.ListView):
    template_name = 'music/outfits.html'
    context_object_name = 'outfit_list'

    def get_queryset(self):
        """
        Return all outfits (not including those set to be
        published in the future).
        """
        return Outfit.objects.all()


class OutfitView(generic.DetailView):
    model = Outfit
    template_name = 'music/outfit.html'
    context_object_name = 'outfit'

    def get_queryset(self):
        """
        Excludes any outfits that aren't published yet.
        """
        return Outfit.objects.all()


class AlbumView(generic.DetailView):
    model = Album
    template_name = 'music/album.html'
    context_object_name = 'album'

    def get_queryset(self):
        """
        Excludes any albums that aren't published yet.
        """
        return Album.objects.filter(pub_date__lte=timezone.now())


class TrackView(generic.DetailView):
    model = Track
    template_name = 'music/track.html'
    context_object_name = 'track'

    def get_queryset(self):
        """
        Excludes any tracks that aren't published yet.
        """
        return Track.objects.filter(pub_date__lte=timezone.now())
