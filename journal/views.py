from django.http import Http404
from django.shortcuts import render

from .models import JournalEntry


def index(request):
    latest_entry_list = JournalEntry.objects.order_by('-pub_date')[:5]
    context = {'latest_entry_list': latest_entry_list}
    return render(request, 'journal/index.html', context)

def entry(request, journal_entry_id):
    try:
        journal_entry = JournalEntry.objects.get(pk=journal_entry_id)
    except JournalEntry.DoesNotExist:
        raise Http404("Journal entry does not exist")
    return render(request, 'journal/entry.html',
                  {'journal_entry': journal_entry})
