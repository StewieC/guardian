from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_incident, name='report_incident'),
    path('incidents/', views.incident_list, name='incident_list'),
    path('articles/', views.article_list, name='article_list'),
    path('contact/', views.contact_authorities, name='contact_authorities'),
    path('file-case/', views.file_case, name='file_case'),
    path('find-lawyer/', views.find_lawyer, name='find_lawyer'),
]