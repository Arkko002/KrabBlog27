from django.test import TestCase
from django.urls import reverse
from blogasek.models import *


# Create your tests here.
class IndexViewTests(TestCase):

    def test_no_posts(self):
        """If no posts exist, an appropriate message is displayed."""

        response = self.client.get(reverse("blogasek:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
