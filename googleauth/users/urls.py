from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard")
]
