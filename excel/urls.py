from django.urls import path
from . import views
urlpatterns = [
    path('prueba/',views.export_users_csv,name='export_users_csv'),
    path('shows/',views.export_shows,name='export_shows'),
]
