import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Python', response.data)

    def test_contact_status(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_has_name(self):
        response = self.app.get('/contact')
        self.assertIn(b'Douglas Masotti', response.data)

    def test_contact_has_email_link(self):
        response = self.app.get('/contact')
        self.assertIn(b'mailto:', response.data)
        self.assertIn(b'dmasotti@adobe.com', response.data)

    def test_contact_has_address(self):
        response = self.app.get('/contact')
        self.assertIn(b'San Francisco', response.data)

    def test_contact_has_social_links(self):
        response = self.app.get('/contact')
        self.assertIn(b'LinkedIn', response.data)
        self.assertIn(b'GitHub', response.data)
        self.assertIn(b'Twitter/X', response.data)
        self.assertIn(b'Instagram', response.data)

    def test_contact_social_links_open_in_new_tab(self):
        response = self.app.get('/contact')
        self.assertIn(b'target="_blank"', response.data)
        self.assertIn(b'rel="noopener noreferrer"', response.data)

    def test_contact_nav_link_present(self):
        response = self.app.get('/')
        self.assertIn(b'/contact', response.data)

if __name__ == '__main__':
    unittest.main()