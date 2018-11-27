from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_status_code(self):
        """Root url return status code 200"""
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        """Page loads with correct html content"""
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertTrue(
            b'<a class="navbar-brand" href="#">Wish Tree</a>' in response.data)

    def test_index_post_request(self):
        """After sending post request, new Feature gets added into page"""
        tester = app.test_client(self)
        response = tester.post('/', data=dict(featureTitle="Test Title", featureDescription="Test Description", featureClient="Client A",
                                              featureClientPriority=1, featureTargetDate="9999-12-31", featureProductArea="Policies"), follow_redirects=True)
        self.assertIn(b'9999-12-31', response.data)


if __name__ == "__main__":
    unittest.main()
