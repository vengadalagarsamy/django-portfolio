from django.shortcuts import render, get_object_or_404
from .models import Blogpost

#order blogposts by date
def all_blogs(request):
    blogposts = Blogpost.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogposts':blogposts})

#when a blog post is clicked, redirect to a page with the full post
def detail(request, blog_id):
    blog = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'blog/detail.html', {'post':blog})
