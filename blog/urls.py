from django.urls import path
from . import views

"""
Note: '<int:pk>' allows for a variable appendage to the base url.
This appendage is a random integer value pulled from the 'pk' argument
fed to an Django template url call. The 'pk' stands for "primary key".
"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

"""
Django Workflow (from what I gather after doing DjangoGirls tutorial):
1. Create a new url path for any branches to your website in 'urls.py' of your website's main directory
2. Create a respective view for said url in 'views.py' of the same directory.
3. Add a new template file to your templates sub-directory within the parent directory of your website
   (i.e. how all templates in this tutorial are under 'blog/templates/blog' rather than simply 'blog'
   like 'urls.py' and 'views.py' are.)
4. Use Django's url template to link a url to anchors in HTML code
5. Use Django block content's to stylize content within a url link's webpage
"""

