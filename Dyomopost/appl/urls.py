from django.urls import path
from .views import *

app_name = 'appl'

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>', PostDetailView.as_view()),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>', CommentDetailView.as_view()),
]
