from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser."""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom User model with email as the unique identifier."""
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_groups', # related name
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_permissions',
        blank=True,
    )

    USERNAME_FIELD = 'email'  # Use email for authentication instead of username
    REQUIRED_FIELDS = []  # No additional fields required for creating a superuser

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def profile_url(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return url
