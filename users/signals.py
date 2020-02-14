from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#**kwargs = accept any additional parameter
#Signal (function) that is sent when an action is performed (user created)

# When a user is saved -> execute def create_profile
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs) :
    #Functionalty to execute every time a profile is created
    if created :
        #Execute class Profile constructor to create a new user
        Profile.objects.create(user = instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
