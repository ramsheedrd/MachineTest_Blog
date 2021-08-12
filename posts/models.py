from django.db import models
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

# Create your models here.


CATEGORY_CHOICES= [
    ('cs', 'Computer Science'),
    ('auto', 'Auto'),
    ('smartphone', 'Smartphones'),
    ('arts', 'Arts'),
    ('sports', 'Sports'),
    ]

class PostModel(models.Model):
    heading = models.CharField(max_length=120)
    tags = TaggableManager()
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES, default='cs')
    content = HTMLField()
    slug = models.SlugField(unique=True, max_length=100)
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.heading

