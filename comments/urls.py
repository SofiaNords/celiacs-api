from django.urls import path
from comments import views

urlpatterns = [
    # Route for listing all comments or creating a new comment
    path('comments/', views.CommentList.as_view()),

    # Route for retrieving, updating, or deleting a specific
    # comment by its primary key (pk)
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]
