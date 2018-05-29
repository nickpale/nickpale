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

    def get_context_data(self, **kwargs):
        context = super(LoopView, self).get_context_data(**kwargs)
        loop_id = context['loop'].id

        context['first_loop'] = Loop.objects.order_by('id').first()
        context['previous_loop'] = Loop.objects.filter(id__lt=loop_id).order_by('-id').first()
        context['next_loop'] = Loop.objects.filter(id__gt=loop_id).order_by('id').first()
        context['latest_loop'] = Loop.objects.order_by('id').last()

        return context
