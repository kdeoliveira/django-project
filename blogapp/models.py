from django.db import models
# Create tables through classes representations for DBs
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#   Methods
    # GET Functions
    # Post.objects.all()
    # Post.objects.filter(author = " Name ").first()
    # Post.objects.get(id=1)
    #
    # MODIFY/ADD Functions
    # Post(title = '', content = '', ....).save()
    # Post(author = User) --> User is an table Object from django.contrib.auth.models
    # 
    # User.(id...).post_set --> Reads posts for a specific user
    # User.get(id...).post_set.create(title, content, ...) --> Creates new post for user

# Post Table
class Post(models.Model):
    title = models.CharField(max_length=99)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    #Links User table to Post table
    # author = User object
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #Override for shell print
        return self.title+" - "+str(self.last_modified)

    #Reverse routing to get url -> returns the full path as String
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    

