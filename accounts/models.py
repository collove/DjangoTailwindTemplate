from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models


class User(BaseUser):
    pass

    def __str__(self):
        return self.username
