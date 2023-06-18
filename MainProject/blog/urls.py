from django.urls import path
from blog.views import bloglist, blog_detail, blog_create

app_name = 'blog'
urlpatterns = [
    path('', bloglist, name='main_blog'),
    path('detail/<int:id>/', blog_detail, name='blog_details'),
    path('create/', blog_create, name='blog_create')
]


