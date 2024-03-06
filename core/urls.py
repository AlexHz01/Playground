from django.urls import path
from .views import HomePageView, samplePageViw

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', samplePageViw.as_view(), name="sample"),
]