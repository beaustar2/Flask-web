import unittest
from app import app  # Import the app instance from your main application file
from flask.testing import FlaskClient

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Use the app instance from your main application file for testing
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World!', response.data)
        self.assertIn(b'Welcome to my aspiring journey', response.data)

    def test_projects_route(self):
        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Explore my exciting projects here!', response.data)

    def test_about_route(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Learn more about me and my DevOps journey.', response.data)

    def test_contact_route(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Feel free to reach out to me!', response.data)
        self.assertIn(b'Phone: +1 (555) 123-4567, Email: info@example.com', response.data)

if __name__ == '__main__':
    unittest.main()

