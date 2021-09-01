from django.urls import path
from . import views

urlpatterns = [
    # GETS
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.agregar),
    path('shows/<int:id>/edit', views.editar),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/delete', views.borrar),

    # POSTS
    path('shows/create', views.crear_show),


]
