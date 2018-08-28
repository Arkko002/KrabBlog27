from django.shortcuts import redirect
import django.views.generic as generic
from django.utils import timezone
from .models import *
from . import forms


# Create your views here.
class IndexView(generic.ListView):
    model = BlogPost
    template_name = "blogasek/index.html"

    def get_queryset(self):
        return BlogPost.objects.order_by("pub_date")


class DetailView(generic.DetailView):
    model = BlogPost
    template_name = "blogasek/detail.html"


class UserView(generic.DetailView):
    model = User
    template_name = "blogasek/user.html"


class CreatePost(generic.CreateView):
    model = BlogPost
    fields = ["text", "title"]
    template_name = "blogasek/create_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.pub_date = timezone.now()
        post.save()
        return redirect("detail", pk=post.pk)


class CreateComment(generic.CreateView):
    form_class = forms.CommentForm
    template_name = "blogasek/create_comment.html"

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.blog_post = BlogPost.objects.get(pk=self.kwargs["pk"])
        comment.pub_date = timezone.now()
        comment.save()
        return redirect("detail", pk=comment.blog_post.pk)


class UpdatePost(generic.UpdateView):
    model = BlogPost
    fields = ["text", "title"]