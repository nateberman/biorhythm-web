from django.test import TestCase
from django.test import Client

# Create your tests here.
class MakewaveTestCase(TestCase):
	def test_makewave(self):
		"""GET a biorhythm wave"""
		c = Client()
		response = c.get('/makewave/', {'year':1982, 'month':03, 'day':10})
		self.assertEqual(response.status_code, 200)

	def test_makewave(self):
		"""A POST to makewave should fail"""
		c = Client()
		response = c.post('/makewave/', {'year':1982, 'month':03, 'day':10})
		self.assertEqual(response.status_code, 404)	