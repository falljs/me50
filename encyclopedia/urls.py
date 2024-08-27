from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("create/", views.create_entry, name="create_entry"),
    path("<str:title>/edit/", views.edit_entry, name="edit_entry"),
    path("random/", views.random_entry, name="random_entry"),  # Nouvelle URL pour la page aléatoire
]
