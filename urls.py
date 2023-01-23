from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
  path('', views.schedule_index, name='schedule_index'),
  path("add/", views.add_event, name="add_event"),
  path("list/", views.get_events, name="get_events"),
  path('detail/<int:pk>/', views.schedule_detail, name='schedule_detail'),
  path('update/<int:pk>/', views.schedule_update, name='schedule_update'),
  path('delete/<int:pk>/', views.schedule_delete, name='schedule_delete'),
]