from django.test import TestCase
from django.urls import reverse


class TopicUrlTests(TestCase):
    def test_topic_detail_url_resolves(self):
        self.assertEqual(reverse('Learning_Logs:topic', args=[1]), '/topics/1/')

    def test_home_link_renders_to_the_index_page(self):
        response = self.client.get('/topics/')
        self.assertContains(response, 'href="/"')
