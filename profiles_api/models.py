from django.db import models
from django.contrib.auth.models import AbstractBaseUser
### Used for overriding the default permissions
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    Usef to modify User objects and model where it is used.
    """

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        # Normalize the input emails, capital letters to small letters
        email = self.normalize_email(email)
        # Create new model,setting email,name
        user = self.model(email=email, name =name)

        # Set hashed values for password, encrypted
        user.set_password(password)
        # Set a database, standard way of saving in django
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """
        Create and save a new superuser with given details.
        Similar to admin user
        """
        user = self.create_user(email,name,password)
        # Automatically created by PermissionsMixin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
    Database model for users in the system
    """
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
        """
        Return string representation of our user.
        Required when converting UserProfile object to string
        """
        return self.email
