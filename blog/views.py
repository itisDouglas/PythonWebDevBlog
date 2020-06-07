from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

#template view for about.html
class AboutView(TemplateView):
    template_name = "about.html"


#template view for post.html
class PostView(ListView):
    model = Post
    template_name = "post.html"
