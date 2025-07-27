from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index), #home route
    path("createblog/",views.createblog),
    path("myblog/", views.myblog)
]
