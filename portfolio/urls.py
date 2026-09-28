from django.urls import path
from . import views
urlpatterns=[
 path('',views.home,name='home'), path('projects/',views.projects,name='projects'), path('projects/<slug:slug>/',views.project_detail,name='project_detail'),
 path('adventures/',views.adventures,name='adventures'), path('adventures/<slug:slug>/',views.adventure_detail,name='adventure_detail'),
 path('posts/',views.posts,name='posts'), path('posts/<slug:slug>/',views.post_detail,name='post_detail'),
]
