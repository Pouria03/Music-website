from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Group
# 

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


    def create_pro_user(self,email,is_pro,password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.is_pro = True
        premium_users = Group.objects.get(name='premium_users') 
        premium_users.user_set.add(user)
        user.save(using=self._db)
        return user
