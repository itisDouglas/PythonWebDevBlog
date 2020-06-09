from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

# Create your views here.
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

#template view for about.html
class AboutView(TemplateView):
    template_name = "about.html"


#detail view for post.html
class PostView(DetailView):
    model = Post
    template_name = "post.html"
