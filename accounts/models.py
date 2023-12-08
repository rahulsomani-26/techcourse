from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("Email is Mandatory")
        if not username:
            raise ValueError('Username Mandatory')
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,first_name,last_name,username,email,password=None):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user 
    
class User(AbstractBaseUser):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects = UserManager()
    

    def __str__(self):
        return f'{self.email}'

    def has_perm(self,perm,obj):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True




