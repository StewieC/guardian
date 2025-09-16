from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Dashboard
    path('report/', views.report_incident, name='report_incident'),
    path('incidents/', views.incident_list, name='incident_list'),
    path('articles/', views.article_list, name='article_list'),
]