from django.test import TestCase

class BotViewTest(TestCase):
    def test_post_message(self):
        response = self.client.post('/bot/handle/', {'message': 'Hello!'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You: Hello!')

    def test_post_empty_message(self):
        response = self.client.post('/bot/handle/', {'message': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a weather related message')