from django.urls import path
from category import views


# URL patterns for the category app
urlpatterns = [
    # URL pattern for the list of categories, handled by CategoryList view
    path('category/', views.CategoryList.as_view()),
    # URL pattern for a specific category, identified by its primarey key (pk)
    # handled by CategoryDetail view
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
]
