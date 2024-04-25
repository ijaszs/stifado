from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now
from django.utils import timezone

# Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    address = models.CharField(max_length=255)
    opening_time = models.TimeField(default=now().replace(hour=9, minute=0, second=0, microsecond=0))  # Default to 9:00 AM
    closing_time = models.TimeField(default=now().replace(hour=22, minute=0, second=0, microsecond=0))  # Default to 10:00 PM
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_active(self):
        """Return True if current time is within opening and closing times."""
        from django.utils import timezone
        current_time = timezone.localtime(timezone.now()).time()
        return self.opening_time <= current_time < self.closing_time

    def __str__(self):
        return self.name
    
class OpeningHours(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="opening_hours")
    day_of_week = models.IntegerField()  # 0=Monday, 6=Sunday
    open_time = models.TimeField()
    close_time = models.TimeField()

    def is_now_open(self):
        from django.utils import timezone
        current_time = timezone.localtime(timezone.now()).time()
        current_weekday = timezone.localtime(timezone.now()).weekday()
        return self.day_of_week == current_weekday and self.open_time <= current_time < self.close_time


#Product model
class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    DIETARY_CHOICES = [
        ('V', 'Vegetarian'),
        ('N', 'Non-Vegetarian'),
    ]
    dietary_choices = models.CharField(max_length=1, choices=DIETARY_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="product_images" ,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.name

# Image model
class Image(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="restaurant_images", null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.restaurant.name} - {self.created_at}"


# Custom user model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# User Rating model  
class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating_value = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('restaurant', 'user')

# Offers model
class Offer(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    offers = models.IntegerField(default=0, help_text="Discount on the restaurant in percentage")
    offer_description = models.CharField(max_length=255)
    offer_validity_start = models.DateTimeField()
    offer_validity_end = models.DateTimeField()

   
    def is_valid(self):
        now = timezone.now()
        return self.offer_validity_start <= now <= self.offer_validity_end

    def __str__(self):
        return self.offer_description

# Category model
class Category(models.Model):
    Product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories_images", null=True,blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
            return self.name
    


    
