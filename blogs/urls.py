from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
                    

app_name = 'Blogs'
urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-create'), 
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<slug:slug>/edit/', BlogUpdateView.as_view(), name='blog-edit'),
    path('blog/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog-delete'),  
]