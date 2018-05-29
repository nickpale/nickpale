import json

from django.test import TestCase
from unittest import mock

from .models import PushNotification


TEST_URL = 'http://example.com/message'
TEST_HEADERS = json.dumps({"Content-Type": "application/json"})


def create_notification(message):
    """Creates a notification with given `message`"""
    return PushNotification.objects.create(url=TEST_URL,
                                          data=message,
                                          headers=TEST_HEADERS)


class PushNotificationTests(TestCase):
    @mock.patch('requests.post')
    def test_send_one_notification(self, post_request):
        """PushNotification.send() sends one notification"""
        create_notification(json.dumps({"message": "hello"}))
        self.assertEqual(PushNotification.objects.count(), 1)

        post_request.return_value.status = 200
        post_request.return_value.text = 'Success!'

        response = PushNotification.send()

        post_request.assert_called_once()
        self.assertEqual(len(response[TEST_URL]), 1)
        self.assertEqual(response[TEST_URL][0].status, 200)
        self.assertEqual(response[TEST_URL][0].text, 'Success!')

    @mock.patch('requests.post')
    def test_send_multiple_notifications(self, post_request):
        """PushNotification.send() sends multiple notifications"""
        for i in range(3):
            create_notification(
              json.dumps({"message": "hello{number}".format(number=i)})
            )
        self.assertEqual(PushNotification.objects.count(), 3)

        post_request.return_value.status = 200
        post_request.return_value.text = 'Success!'

        responses = PushNotification.send()

        self.assertEqual(post_request.call_count, 3)
        self.assertEqual(len(responses[TEST_URL]), 3)
        for i in range(3):
            self.assertEqual(responses[TEST_URL][i].status, 200)
            self.assertEqual(responses[TEST_URL][i].text, 'Success!')
