from django.urls import path
from posts import views


# URL patterns for the posts app
urlpatterns = [
    # URL pattern for the list of posts, handled by PostList view
    path('posts/', views.PostList.as_view()),
    # URL pattern for a specific post, identified by its primary key (pk)
    # handled by PostDetail view
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]
