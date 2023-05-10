"""
- What is Django URLs?make program to create django urls?
# myapp/urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
    ]

  we define three URL patterns for the myapp app. The path function takes two arguments: 
  the URL pattern as a string, and the view function that should be called when the URL pattern is matched.

"""