import os.path
from django.test import TestCase
from .models import WallPaper
from io import BytesIO
from PIL import Image
from django.core.files import File



class WallpaperModelTest(TestCase):

    @staticmethod
    def get_image_file(name='honda_tohru', ext='jpeg', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGB", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        WallPaper.objects.create(title='honda-tohru', image=WallpaperModelTest.get_image_file(), tag='fruit-basket', is_nsfw=False)


    def test_title_content(self):
        obj = WallPaper.objects.get(id=1)
        expected_obj_name = f'{obj.title}'
        self.assertEqual(expected_obj_name, 'honda-tohru')

    def test_tag(self):
        obj = WallPaper.objects.get(id=1)
        expected_tag = f'{obj.tag}'
        self.assertEqual(expected_tag, 'fruit-basket')

    def test_is_nsfw(self):
        obj = WallPaper.objects.get(id=1)
        expected = f'{obj.is_nsfw}'
        self.assertEquals(expected, 'False')


    def test_image(self):
        obj = WallPaper.objects.get(id=1)
        expected_image = f'{obj.image}'
        _image = self.get_image_file().name
        if os.path.isfile(f"wallpapers/{_image}"):
            os.remove(f"wallpapers/{_image}")
        self.assertEqual(expected_image, _image)