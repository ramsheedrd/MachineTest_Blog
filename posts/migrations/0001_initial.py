# Generated by Django 3.2.6 on 2021-08-12 10:50

from django.db import migrations, models
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('content', tinymce.models.HTMLField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('published', models.DateField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
