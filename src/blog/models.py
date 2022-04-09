import imp
from tabnanny import verbose
from django.db import models

from organiser.models import Startup, Tag

class Post(models.Model):
    
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    text = models.TextField()
    pud_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]
        verbose_name = "blog post"
    
    def __str__(self) -> str:
        date_string = self.pud_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
