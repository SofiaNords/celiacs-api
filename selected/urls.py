from django.urls import path
from selected import views

urlpatterns = [
    path('selected/', views.SelectList.as_view()),
    path('selected/<int:pk>/', views.SelectDetail.as_view()),
]