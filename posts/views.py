from django.views.generic import (
    ListView,
    DetailView
)
from .models import Post

class PostListView(ListView):
    """
    PostListView is foing to retrieve all of the objects from the Post table in the db
    """

    # template_name attribute is going to render an specific html file
    template_name = "posts"
    # model is foing to be from which table we want to retrieve the data
    model = Post
    # context_object_name allows us to modify the name on how we call it in the htmls
    context_object_name = "posts"