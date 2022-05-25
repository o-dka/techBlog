from django.urls import path
from . import views 

urlpattern = [
        path('', views.post_list, name='post_list'),
]
