from django.db import models


class facebookdata(models.Model):
    user_id = models.IntegerField(11)
    posts = models.TextField()
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

