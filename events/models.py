from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=True, blank=True, max_length=225)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(null=True, blank=True, max_length=80)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True,max_length=225,unique=True)
    web_source = models.CharField(null=True, blank=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Events"
        ordering = ['title']

