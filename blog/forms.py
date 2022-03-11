# from socket import fromshare
from django import forms
from .models import Post

"""
Param. forms.ModelForm takes an instance of a  Django model we've defined
(i.e. 'Post') and converts it into a Django form.

The 'Meta' sub-class confirms what 'model' is anticipated and what fields
of said model should be able to be manipulated when viewing this form. For
security reasons, only fields that should be accessible to the viewer for
editing should be listed here.

Note: After creating a Django form, you need to create a view for it
in the parent directory's 'views.py' file. Also, for every Django view,
you will need a respective url path in the 'urls.py' file within the same
directory.
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post # Tell Django to use our 'Post' object as the model used to create this form
        fields = ('title', 'text',) # Contains all fields in the input model to be edited by this form

"""
Note: Also know that you need to do several things in the HTML file containing
a Django form (said HTML file is the webpage your respective view for said form
you to to view the form):
    1. Display the form (use the Django braces technique in your HTML file)
    2. The line above the form display line needs to be wrapped with an HTML
       'form' element i.e. <form method="POST">...</form>
    3. A save button (can typically do by adding an HTML button element:
       <button type="submit">Save</button>) (button must be in the ... of
       the <form></form> element mentioned in step 2)
    4. Add {% csrf_token %} right after the <form> HTML tag for security
       reasons (not after <form>...</form>, but rather immediately after
       the first <form> tag.)
"""