from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post # The '.' in front of 'models' module means "relative/local" library
                         # it's referencing the models.py file in this same directory.

# Create your views here.
def post_list(request):
    # Get a QuerySet (an array of data from our Django framework's database) containing all
    # posts that meet the following filters:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns a Post object if valid primary key provided, otherwise 404 error page returned
    return render(request, 'blog/post_detail.html', {'post': post})
