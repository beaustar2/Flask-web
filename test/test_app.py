import unittest
from app import app, db, User
from flask.testing import FlaskClient
from flask_login import login_user, current_user
from bs4 import BeautifulSoup

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        if not hasattr(self.app, 'extensions') or 'sqlalchemy' not in self.app.extensions:
            db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def create_test_user(self):
        with self.app.app_context():
            test_user = User(username='test_user')
            db.session.add(test_user)
            db.session.commit()

    def login_test_user(self):
        response = self.client.post('/login', data=dict(username='test_user'))

        # Check if the login was successful
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect after successful login
        expected_url = 'http://localhost:5000/'  # Update this with your app's actual URL
        self.assertTrue(response.location.startswith(expected_url))

        # Follow the redirect to the home page
        response = self.client.get(response.location)
        self.assertEqual(response.status_code, 200)  # 200 indicates a successful GET request
        self.assertIn(b'Welcome', response.data)  # Assuming the home page contains 'Welcome'

        # Check if the user is logged in
        with self.app.app_context():
            user = User.query.filter_by(username='test_user').first()
            login_user(user)

        self.assertTrue(current_user.is_authenticated)

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to our aspiring journey', response.data)

    def test_projects_route(self):
        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Explore our exciting projects here!', response.data)

    def test_about_route(self):
        response = self.client.get('/Aboutus')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Learn more about us and our DevOps journey.', response.data)

    def test_contact_route(self):
        response = self.client.get('/Contactus')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Feel free to reach out to us!', response.data)
        self.assertIn(b'Phone: +1 (555) 123-4567, Email: info@devopsjourney.com', response.data)

if __name__ == '__main__':
    unittest.main()
