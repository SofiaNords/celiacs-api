from django.urls import path
from profiles import views

# URL patterns for the profiles app
urlpatterns = [
    # URL pattern for the list of profiles, handled by ProfileList view
    path('profiles/', views.ProfileList.as_view()),
    # URL pattern for a specific profile, identified by its primary key (pk)
    # handled by ProfileDetail view
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]
