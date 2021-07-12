from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='base-page'),
    path('message/<int:pk>/', PostDetailView.as_view(), name='message-detail'),
    path('message/new/', PostCreateView.as_view(), name='message-create'),
]