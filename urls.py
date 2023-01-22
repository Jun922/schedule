from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
  path('', views.schedule_index, name='schedule_index'),
  path("add/", views.add_event, name="add_event"),
  path("list/", views.get_events, name="get_events"),
]