from django.test import TestCase
from .models import Image


class ImageModelTest(TestCase):
    fixtures = ['file json']

    def create_image(self):
        return Image.objects.create(source='test_image',
                                    correct_label=0,
                                    uploaded_by=1,
                                    filename='../media/2418_class-1.png')

    def test_create_image(self):
        im = self.create_image()
        self.assertTrue(isinstance(im, Image))
