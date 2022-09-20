from django.db import models
from external.abstracts.models import BaseModel
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager


# Create your models here.

class User(BaseModel, AbstractUser):
    username = models.CharField(max_length=20, blank=True, null=True, help_text="username of a user")
    email = models.EmailField(unique=True, blank=False, null=False, help_text="User personal email address")
    last_pass_change = models.DateTimeField(blank=True, null=True, help_text="Last password changed date")
    auth_token = models.CharField(max_length=6, null=True, help_text="authentication code")
    two_factor = models.BooleanField(default=False, help_text='Activates two factor auth')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
