"""Defining URL pattern for Learning Log"""
from django.urls import path
from . import views

app_name = 'Learning_Logs'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # page that will show all topics
    path('topics/', views.topics, name='topics'),
    # Details page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
