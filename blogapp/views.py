from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

#------------------------------------------------
# DB representation via dictionary
#Send DB info to webpage
posts = [
    {
        'author': 'CpreyMS',
        'title': 'BLog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Shakespeare',
        'title': 'BLog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'July 20, 2018'
    }
]

def testDB(request):

    #dictionary of dictionary for posts variable
    context = {
        'title': "About Us",  # Sending title for HTML page
        'posts': posts
    }
    #HTML page location from TEMPLATES folder
                    #Send context (dictionary) data to index.html

    return render(request, 'blog/test.html', context)


@login_required
def home(request):
    context = {'posts': Post.objects.all()}  # imorts all posts
    return render(request, 'blog/index.html', context)
#------------------------------------------------------------ END TEST




#Import DB tables
    #.models -> models of current directory
from .models import Post
#Generic views built-in by django
from django.views.generic import (ListView, 
                                    DetailView, 
                                        CreateView, 
                                            UpdateView, 
                                                DeleteView)
# @login_required for Classes                               #Certifies if same user access a webpage of its own
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


#Generic view for PAGES
# Uses generic built-in views 
# URLS paths are craeting wihtin the class

class PostListView(ListView):       #HOME PAGE
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'   # Default value: object     -> Value called on html 
    ordering = ['-date_posted']     # Order to fetch data
    paginate_by = 5                 #Paginator object/attribute


class UserPostListView(ListView):  # USER POSTS PAGE
    model = Post
    template_name = 'blog/post_user.html'
    context_object_name = 'posts'   
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, DetailView):       #POST/<PK> PAGE
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin,CreateView):        #NEW POST PAGE
    model = Post
    template_name = 'blog/post_create.html'
    context_object_name = 'posts'
    fields = ['title', 'content']

    #  success_url = 'blog_home'    -> Redirect after submit || Otherwise: models.py -> get_absolute_url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_create.html'
    context_object_name = 'posts'
    fields = ['title', 'content']

    #  success_url = 'blog_home'    -> Redirect after submit || Otherwise: models.py -> get_absolute_url

    def form_valid(self, form):
        form.instance.author = self.request.user
                                                    # form.instance -> represents Post model (DB table)
                                                    # form.instance.author -> linked to User model (DB table)
        messages.success(self.request, f'Your post #{form.instance.id} has been updated')
        return super().form_valid(form)

        #Mandatory method to get current object
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    context_object_name = 'posts'

    def get_success_url(slef):
        return reverse('blog_home')
    #Alternative method:
    # from django.urls import reverse_lazy
    # success_url = reverse_lazy('blog_home')      -> Converts url variable into full path String
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#OTHER PAGES

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
