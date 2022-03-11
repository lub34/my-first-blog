# from msvcrt import kbhit # I think this line is an accident but afraid to delete
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Post # The '.' in front of 'models' module means "relative/local" library
                         # it's referencing the models.py file in this same directory.
from .forms import PostForm

# Create your views here.
def post_list(request):
    # Get a QuerySet (an array of data from our Django framework's database) containing all
    # posts that meet the following filters:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    # Note: The braces argument at the end of render specifies how to format the
            # QuerySet that render will return (in this case, it'll store all the
            # posts on post_list.html).

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns a Post object if valid primary key provided, otherwise 404 error page returned
    return render(request, 'blog/post_detail.html', {'post': post})

"""
For the following view, we need two different views:
    1. The user is making a new post.
    2. If the user has just submitted said new post, have them go to the
       view with all the data that was just typed.
"""
def post_new(request):
    if request.method == "POST": # This request method is specified in an HTML form element
         # Fill the post-form with data from the newly filled out form
        form = PostForm(request.POST)
   
        # Then check if the form is valid so we can save it
        if form.is_valid():
            post = form.save(commit=False) # Save the contents of the form, but 
                                           # don't save this instance of a Post model 
                                           # yet; first add details (author, publish_date)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()                    # Now can save this instance of a Post model
            return redirect('post_detail', pk=post.pk) # Redirect to view-page showing post details
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    # Observe how you need to create an html file containing the web-page
    # that wll be viewed using the request for this view.

def post_edit(request, pk):
    # Get Post model being refereced by the pk (primary key)
    post = get_object_or_404(Post, pk=pk) # Need this every time a primary key is used in a view request
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # Pass a copy of the post being edited as an instance
                                                     # of the post before the edit request
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post) # Has the user view the post to be edited.
                                       # The 'if' scenario above it allows the user to
                                       # save and see their edited post.
    return render(request, 'blog/post_edit.html', {'form': form})
