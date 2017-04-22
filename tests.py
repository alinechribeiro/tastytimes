from django.test import TestCase
from .models import Post

class PostTests(TestCase):
	"""
	Here I'll define the tests
	that I'll run against my Post model
	"""

	def test_str(self): 
		test_title = Post(title='My Latest Blog Post')
		self.assertEqual(str(test_title),
		'My Latest Blog Post')