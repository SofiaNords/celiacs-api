from django.urls import path
from selected import views

# URL patterns for the selected app
urlpatterns = [
    # URL pattern for the list of selected items, handled by SelectList view
    path('selected/', views.SelectList.as_view()),
    # URL pattern for a specific selected item, identified by its primary key
    # (pk) handled by SelectDetail view
    path('selected/<int:pk>/', views.SelectDetail.as_view()),
]
