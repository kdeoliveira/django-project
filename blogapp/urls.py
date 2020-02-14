from django.urls import path
from . import views


# name: var name of the route 
# used as href

# '': sub_url/directory over main urls.py

urlpatterns = [
    #main page: localhost:8000/blog/

    # path('', views.home, name = 'blog_home'),
    path('', views.PostListView.as_view(), name = 'blog_home'),
                #Variable primary key as int into URL
                # pk is defined in class ListView
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name = 'post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post_delete'),
    path('post/<str:username>/', views.UserPostListView.as_view(), name = 'post_user'),

    path('about/', views.about, name= 'blog_about'),
    #Test page for HTML-PYTHON coding
    path('test.html', views.testDB, name='test'),
]
