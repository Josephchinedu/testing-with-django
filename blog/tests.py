from django.test import TestCase
from .models import Post


# Create your tests here.
class ModelTesting(TestCase):
    def setUp(self) -> None:

        self.blog = Post.objects.create(title='Blog', author='Author', slug='blog')

    def test_post_model(self):
        self.assertEqual(self.blog.title, 'Blog')
        self.assertEqual(self.blog.author, 'Author')
        self.assertEqual(self.blog.slug, 'blog')
