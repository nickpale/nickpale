from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import JournalEntry


class IndexView(generic.ListView):
    template_name = 'journal/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        return JournalEntry.objects.order_by('-pub_date')[:5]

class EntryView(generic.DetailView):
    model = JournalEntry
    template_name = 'journal/entry.html'
    context_object_name = 'journal_entry'
