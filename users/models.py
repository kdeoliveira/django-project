#User model
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Profile(models.Model):
    # One to one relationship between User DB and users app's model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
                # New user field
                # Generates a image automatically for user (default)
                #                       default user.jpg        directory to save picture
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{ self.user.username }\'s profile'

    #DEV ENV SETUP
    #Override save method
    # resize pictures saved on image fields
    #def save(self):
    #    super().save()
    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
