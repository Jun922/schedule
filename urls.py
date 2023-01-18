from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
  path('', views.schedule_list, name='schedule_list'),
  path("add/", views.add_event, name="add_event"),
    path("list/", views.get_events, name="get_events"),
]