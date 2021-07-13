from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='base-page'),
    path('message/new/', PostCreateView.as_view(), name='message-create'),
    path('message/', PostDetailView.as_view(), name='message-detail'),
    path('message/delete', PostDeleteView.as_view(), name='message-delete'), 
    path('message/new/', PostCreateView.as_view(), name='message-create'),
]