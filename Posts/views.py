from django.shortcuts import render, redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
 
class PostListView(ListView):
 
    # specify the model for list view
    model = Post

    def get_queryset(self, *args, **kwargs):
        qs = super(PostListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-date_published")
        return qs

def SearchView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        posts = Post.objects.filter(Title__contains=title)
        return render(request, "Posts/post_list.html", {"object_list":posts})
    else:
        return redirect('/')

class PostView(DetailView):
    model = Post