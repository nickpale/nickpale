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
        Return all outfits (not including those set to be
        published in the future).
        """
        return Outfit.objects.all()

    # did this to use multiple slugs in the urls
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get('outfitslug', None)
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
            # If none of those are defined, it's an error.
        else:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class AlbumView(generic.DetailView):
    model = Album
    template_name = 'music/album.html'
    context_object_name = 'album'

    def get_queryset(self):
        """
        Excludes any albums that aren't published yet.
        """
        return Album.objects.filter(pub_date__lte=timezone.now())

    # did this to use multiple slugs in the urls
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get('albumslug', None)
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
            # If none of those are defined, it's an error.
        else:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class TrackView(generic.DetailView):
    model = Track
    template_name = 'music/track.html'
    context_object_name = 'track'

    def get_queryset(self):
        """
        Excludes any tracks that aren't published yet.
        """
        return Track.objects.filter(pub_date__lte=timezone.now())

    # did this to use multiple slugs in the urls
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get('trackslug', None)
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
            # If none of those are defined, it's an error.
        else:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj
