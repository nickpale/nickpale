import datetime

from django.urls import reverse
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


def create_entry(entry_text, days):
    """
    Creates an entry with the given `entry_text` and published the
    given number of `days` offset to now (negative for entries published
    in the past, positive for entries that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return JournalEntry.objects.create(entry_text=entry_text, pub_date=time)


class JournalEntryViewTests(TestCase):
    def test_index_view_with_no_entries(self):
        """
        If no entries exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('journal:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No entries are available.")
        self.assertQuerysetEqual(response.context['latest_entry_list'], [])

    def test_index_view_with_a_past_entry(self):
        """
        Entries with a pub_date in the past should be displayed on the
        index page.
        """
        create_entry(entry_text="Past entry.", days=-30)
        response = self.client.get(reverse('journal:index'))
        self.assertQuerysetEqual(
            response.context['latest_entry_list'],
            ['<JournalEntry: Past entry.>']
        )

    def test_index_view_with_a_future_entry(self):
        """
        Entries with a pub_date in the future should not be displayed on
        the index page.
        """
        create_entry(entry_text="Future entry.", days=30)
        response = self.client.get(reverse('journal:index'))
        self.assertContains(response, "No entries are available.")
        self.assertQuerysetEqual(response.context['latest_entry_list'], [])

    def test_index_view_with_future_entry_and_past_entry(self):
        """
        Even if both past and future entries exist, only past entries
        should be displayed.
        """
        create_entry(entry_text="Past entry.", days=-30)
        create_entry(entry_text="Future entry.", days=30)
        response = self.client.get(reverse('journal:index'))
        self.assertQuerysetEqual(
            response.context['latest_entry_list'],
            ['<JournalEntry: Past entry.>']
        )

    def test_index_view_with_two_past_entries(self):
        """
        The journal entries index page may display multiple questions.
        """
        create_entry(entry_text="Past entry 1.", days=-30)
        create_entry(entry_text="Past entry 2.", days=-5)
        response = self.client.get(reverse('journal:index'))
        self.assertQuerysetEqual(
            response.context['latest_entry_list'],
            ['<JournalEntry: Past entry 2.>', '<JournalEntry: Past entry 1.>']
        )
