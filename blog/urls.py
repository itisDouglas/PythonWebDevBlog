from django.urls import path

from .views import HomePageView
#create your urls here

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home')
]