from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/<int:id>', views.profile, name="profile"),
    path('profile_edit/', views.profile_edit, name="profile_edit"),
]
