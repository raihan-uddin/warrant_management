from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# Create your models here.
class CustomUser(AbstractUser):
    pass
    # name = models.CharField(max_length=255)
    # email = models.EmailField(max_length=255)
    # # user_name = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)

