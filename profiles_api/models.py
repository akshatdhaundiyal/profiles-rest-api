from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        # Normalize the input emails
        email = self.normalize_email(email)
        user = self.model(email=email, name =name)

        # Set hashed values for password
        user.set_password(password)
        # Set a database, standard way of saving in django
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """ Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # Determine or create staff accounts
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # Instead of having username for creating accounts, use email address
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Functions for django to interact with custom user models

    def get_full_name(self):
        """ Retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user"""
        return self.name

    def __str__(self):
        """ Return string representation of our user"""
        return self.email
