"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#
#         URL_client                 
# path('name/index.hmtl', views.method, variable_name)
#
#         views.py      templates html file
# return render(request, 'name/index.html')

from django.contrib import admin
from django.urls import path, include

#URL for media picture (only for development)
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #Built-in admin page
    path('admin/', admin.site.urls),
    #URLS map for blogapp
    path('blog/', include('blogapp.urls')),
    path('account/', include('users.urls')),
    #Temporary home page
    path('', views.index, name = 'index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)



