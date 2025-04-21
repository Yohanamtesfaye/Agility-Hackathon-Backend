from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group,Permission
from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings

ROLE_CHOICES = [
    ('citizen', 'Citizen'),
    ('authority', 'Authority'),
    ('admin', 'Admin'),
]

GENDER_CHOICES=[
    ('female','Female'),
    ('male','Male'),
]

STATUS_TYPE_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('pending', 'Pending'),
    ('completed', 'Completed'),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Please enter the email address!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id=models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4)
    userName =models.CharField(max_length=255, default='Unknown')
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profile_pic/',blank=True,null=True)
    location = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='citizen')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    groups=models.ManyToManyField(Group,related_name='custom_user_groups',blank=True)
    user_permissions = models.ManyToManyField(Permission,related_name='custom_user_permissions',blank=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

def save(self, *args, **kwargs):
    self.email = self.__class__.objects.normalize_email(self.email)
    super().save(*args, **kwargs)


    def __str__(self):
        return self.email


class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_type = models.CharField(max_length=50, choices=STATUS_TYPE_CHOICES, default='active')
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Status'
        ordering=['-created_at']
        unique_together = ('owner', 'name') 

        
    def __str__(self):
        return self.name


