from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post


class PostView(generic.ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last five published posts (not including those set to be
        published in the future).
        """
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'blog/blog_results.html'