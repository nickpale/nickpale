import json
import requests

from collections import defaultdict

from django.db import models


class PushNotification(models.Model):
    """Holds parameters for making post requests to notification receivers.

    url -- the receiving endpoint ('http://example.com/api/notification')
    data -- the request data in json format ('{"message": "hello"}')
    headers -- the request headers in json format, if needed
               ('{"Content-Type": "application/json"}')
    """
    url = models.TextField()
    data = models.TextField(default='{}')
    headers = models.TextField(default='{}')

    def __str__(self):
        return self.url

    @classmethod
    def send(cls):
        """Sends notification requests to all endpoints."""
        responses_by_url = defaultdict(list)
        for notification in cls.objects.all():
            response = requests.post(notification.url,
                                     json=json.loads(notification.data),
                                     headers=json.loads(notification.headers))
            responses_by_url[notification.url].append(response)
        return responses_by_url

              # json={'channelId': 'da82afad-46f1-48f0-9eef-14eadcacca55-c2b0edea-2558-4ba0-9892-911578d8d789',
              #       'body': 'my notification',
              #       'title': 'django notification'},
              # headers={'Content-Type': 'application/json'})
