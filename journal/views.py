from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import JournalEntry


class JournalIndexView(generic.ListView):
    template_name = 'journal/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        """
        Return all published entries (not including those set to be
        published in the future).
        """
        return JournalEntry.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class JournalEntryView(generic.DetailView):
    model = JournalEntry
    template_name = 'journal/entry.html'
    context_object_name = 'journal_entry'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return JournalEntry.objects.filter(pub_date__lte=timezone.now())
