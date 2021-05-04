from django.db import models




class Portfolio(models.Model):
    name    = models.CharField(max_length=50)
    link    = models.TextField()
    photo   = models.ImageField(upload_to='photo', null=True)
    created_at  = models.DateTimeField(auto_now=True, blank=True)


