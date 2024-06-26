from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth import get_user_model
# User = get_user_model()

import random


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Password is Requared")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_verified = True
        # user.user_type = User.UserType.ADMIN  # Corrected line
        user.user_type = 'admin'

        user.save(using=self._db)
        return user