from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entryPage"),
    path("newEntry", views.newEntry, name="newPage"),
    
]
