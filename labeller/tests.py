from django.test import TestCase
from .models import Image, User


class ImageModelTest(TestCase):
    fixtures = ['a_fixture.json']
    a_user = User.objects.all()[0]

    def create_image(self):
        return Image.objects.create(source='test_image',
                                    correct_label=0,
                                    uploaded_by=self.a_user,
                                    filename='../media/2418_class-1.png')

    def test_create_image(self):
        im = self.create_image()
        self.assertTrue(isinstance(im, Image))
