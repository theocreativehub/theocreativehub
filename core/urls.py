from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracking/', views.tracking, name='tracking'),
    path(
        'download/<str:order_id>/',
        views.download_file,
        name='download_file'
    ),
]