from django.urls import path
from . import views
urlpatterns = [
    path('prueba/<int:id>',views.render_pdf_view,name='reportes_prueba'),
    path('shows/', views.shows, name='reports_shows'),
]
