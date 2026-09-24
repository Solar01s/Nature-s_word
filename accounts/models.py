from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(verbose_name='Real name', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)
    age = models.IntegerField(verbose_name='Age', validators=[MaxValueValidator(0), MaxValueValidator(100)],)
    about = models.CharField(verbose_name='About', max_length=500)

    def __str__(self):
        return f"Profile for {self.user.username}"