from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import PermissionsMixin

from django.conf import settings


#Craeting a user both super user and  normal user
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
         #self.normilize_email #ensures the email is in a proper format (e.g., lowercased).
        #self.model #creates a new instance of the User model
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # hashes the password securely.
        user.set_password(password)
        #Saved the User to the database
        user.save(using=self._db)
        return user
    #Set all use to superuser by default
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


#This is a custom user model that replaces Django’s default one. 
# It inherits from AbstractBaseUser, which gives it password and authentication functionality without using username

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    # Custom manager used to interact with the database using Django's ORM
    objects = UserManager()

    #Instead of logging with username we use email now
    #With dis method
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dob', 'age']


    def __str__(self):
        return self.email



class Task(models.Model):
    STATUS_CHOICES = (
        ('Incomplete', 'Incomplete'),
        ('Complete', 'Complete'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Incomplete')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_name} ({self.status})"