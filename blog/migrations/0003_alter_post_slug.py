# Generated by Django 5.0.1 on 2024-02-04 13:41

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]