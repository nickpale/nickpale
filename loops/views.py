from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Loop


class LoopIndexView(generic.ListView):
    template_name = 'loops/index.html'
    context_object_name = 'latest_loop_list'

    def get_queryset(self):
        """
        Return all published loops (not including those set to be
        published in the future).
        """
        return Loop.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class LoopView(generic.DetailView):
    model = Loop
    template_name = 'loops/loop.html'
    context_object_name = 'loop'

    def get_queryset(self):
        """
        Excludes any loops that aren't published yet.
        """
        return Loop.objects.filter(pub_date__lte=timezone.now())
