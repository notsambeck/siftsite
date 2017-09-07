from .models import Image, User, Choice
from django.test import TestCase, RequestFactory

from .views import label_view, list_view, api_image_list


class ViewsTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@nothing.com', password='top_secret')

    def test_list(self):
        # Create an instance of a GET request.
        request = self.factory.get('/list_view/')

        # Test my_view() as if it were deployed at /customer/details
        response = list_view(request)

        self.assertEqual(response.status_code, 200)

    def test_label(self):
        # Create an instance of a GET request.
        request = self.factory.get('/label_view/')

        # Test my_view() as if it were deployed at /customer/details
        response = label_view(request)

        self.assertEqual(response.status_code, 200)

    def test_api(self):
        # Create an instance of a GET request.
        request = self.factory.get('/api?format=json')

        # Test my_view() as if it were deployed at /customer/details
        response = api_image_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.charset, 'utf-8')


class ImageModelTest(TestCase):
    fixtures = ['a_fixture.json']
    a_user = User.objects.all()[0]

    def create_image(self):
        return Image.objects.create(source='test_image',
                                    correct_label=0,
                                    sift_label=1,
                                    description='test description',
                                    tweeted=True,
                                    uploaded_by=self.a_user,
                                    google_raw_data=str([{'test_descr': 'x'}]),
                                    filename='../media/2418_class-1.png')

    def test_create_image(self):
        im = self.create_image()
        self.assertTrue(isinstance(im, Image))


class ChoiceModelTest(TestCase):
    def create_choice(self):
        c = Choice.objects.create(choice=2, alt_text='two')
        c.save()

    def test_create_choice(self):
        self.create_choice()
        self.assertEqual(Choice.objects.get(choice=2).alt_text, 'two')


class RequestTest:
    fixtures = ['a_fixture.json']

    def test_request_api(self):
        print(requests.request('http://127.0.0.1:8000'))  # noqa
