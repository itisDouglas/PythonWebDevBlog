from django.urls import path

from .views import HomePageView, AboutView, PostView
#create your urls here

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),

    path('about/', AboutView.as_view(), name='about'),
    
    path('post', PostView.as_view(), name='post'),
    
]