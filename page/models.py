from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Third Party Libraries:
from autoslug import AutoSlugField
from tinymce import  models as tinymce_models

# Create your models here.


class Page(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug =  AutoSlugField(populate_from='title', unique=True, )
    title = models.CharField(max_length=200)  
    cover_image = models.ImageField(upload_to='page/', blank=True, null=True)
    #content = models.TextField(blank=True, null=True)
    content = tinymce_models.HTMLField( blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'page:page_view',
            kwargs={
                "page_slug": self.slug

            }
        )
