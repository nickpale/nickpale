import datetime

from django.utils import timezone
from django.test import TestCase

from .models import JournalEntry

class JournalEntryMethodTests(TestCase):

    def test_was_published_recently_with_future_entries(self):
        """
        was_published_recently() should return False for entries whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_entry = JournalEntry(pub_date=time)
        self.assertIs(future_entry.was_published_recently(), False)

    def test_was_published_recently_with_old_entry(self):
        """
        was_published_recently() should return False for entries whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_entry = JournalEntry(pub_date=time)
        self.assertIs(old_entry.was_published_recently(), False)

    def test_was_published_recently_with_recent_entry(self):
        """
        was_published_recently() should return True for entries whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_entry = JournalEntry(pub_date=time)
        self.assertIs(recent_entry.was_published_recently(), True)
