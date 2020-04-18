from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(User):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    title = models.fields.CharField(max_length=200, unique=True, allow_unicode=True)
    slug = models.SlugField(max_length=200,allow_unicode=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    upated_on_time = models.fields.DateTimeField(auto_now=True)
    created_on_time = models.fields.DateTimeField(auto_now=True)
    # status = models.IntegerChoices(choices=STATUS,default=0)
    pass