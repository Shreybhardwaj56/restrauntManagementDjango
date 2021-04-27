from django.urls import path

from . import views

app_name = "restraunt"

urlpatterns = [
    # Create
    path("add/", views.Create.as_view(), name="add"),
    # Read
    path("", views.Index.as_view(), name="index"),
    path("<int:pk>/", views.Details.as_view(), name="details"),
    # Update
    path("<int:pk>/update/", views.Update.as_view(), name="update"),
    # Delete
    path("<int:pk>/delete/", views.Delete.as_view(), name="delete"),
]
