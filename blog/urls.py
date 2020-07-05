from django.urls import path, reverse

from .views import HomePageView, AboutView, PostView, PostSearchResultsListView
#create your urls here

urlpatterns = [

    path('home/', HomePageView.as_view(), name = 'home'),

    path('about/', AboutView.as_view(), name='about'),
    
    path('post/<int:pk>', PostView.as_view(), name='post'),
    #reverse('post'),

    path("search/", PostSearchResultsListView.as_view(), name="search_results"),

    path('', HomePageView.as_view(), name = 'home'),
    
]