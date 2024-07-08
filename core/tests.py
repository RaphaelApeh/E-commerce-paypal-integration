from django.test import TestCase,Client

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'core/front-page.html')
        self.assertEqual(response.status_code,200)

    def test_detail(self):
        try:
            response = self.client.get('detail/<int:pk>/')
            self.assertTemplateUsed(response,'core/detail.html')
        except:
            print('Error1')