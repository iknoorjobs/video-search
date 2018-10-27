from django.urls import path, include
from mainApp import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('vsearch/', views.vid_search_page, name='video_search'),
    path('login/', views.login_page, name='login'),
    path('groups/', views.groups_page, name='groups'),
]
