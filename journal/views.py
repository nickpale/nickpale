from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the journal index.")

def entry(request, journal_entry_id):
    return HttpResponse("You're looking at journal entry %s." % journal_entry_id)
