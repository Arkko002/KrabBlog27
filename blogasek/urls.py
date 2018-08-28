from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:pk>", views.DetailView.as_view(), name="detail"),
    path("detail/<int:pk>/comment/", views.CreateComment.as_view(), name="comment"),
    path("user/<int:pk>", views.UserView.as_view(), name="user"),
    path("create/", views.CreatePost.as_view(), name="create"),
]