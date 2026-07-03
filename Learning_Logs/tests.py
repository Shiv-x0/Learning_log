from django.test import TestCase
from django.urls import reverse

from .models import Topic, Entry


class TopicUrlTests(TestCase):
    def test_topic_detail_url_resolves(self):
        self.assertEqual(reverse('Learning_Logs:topic', args=[1]), '/topics/1/')

    def test_home_link_renders_to_the_index_page(self):
        response = self.client.get('/topics/')
        self.assertContains(response, 'href="/"')

    def test_edit_entry_page_renders(self):
        topic = Topic.objects.create(text='Django Basics')
        entry = Entry.objects.create(topic=topic, text='First entry')

        response = self.client.get(reverse('Learning_Logs:edit_entry', args=[entry.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit entry:')
        self.assertContains(response, 'Save Changes')
