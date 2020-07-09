from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.db.models import Q
from django.urls import reverse

# Create your views here.
from .models import Post
#I have to create my data querying here

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 10
    #queryset = Post.objects.filter(body__icontains="Test")
            
        

#template view for about.html
class AboutView(TemplateView):
    template_name = "about.html"
    


#detail view for post.html
class PostView(DetailView):
    model = Post
    template_name = "post.html"
    

    

#Search post results view
class PostSearchResultsListView(ListView):
    model = Post
    template_name = "search_results.html"
    
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(body__icontains=query) | Q(title__icontains=query)
        )
        return object_list



#define function to get a query set
#use split function to take user input and make each word into list
