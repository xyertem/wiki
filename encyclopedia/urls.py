from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entryPage"),
  # path("search_bar", views.search_bar , name="search_bar")

]
