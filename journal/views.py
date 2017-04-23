from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import JournalEntry


def index(request):
    latest_entry_list = JournalEntry.objects.order_by('-pub_date')[:5]
    context = {'latest_entry_list': latest_entry_list}
    return render(request, 'journal/index.html', context)

def entry(request, journal_entry_id):
    journal_entry = get_object_or_404(JournalEntry, pk=journal_entry_id)
    return render(request, 'journal/entry.html',
                  {'journal_entry': journal_entry})
