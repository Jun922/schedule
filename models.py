from django.db import models

class Event(models.Model):
  start_date = models.DateField()
  end_date = models.DateField()
  event_name = models.CharField(max_length=200)

  def __str__(self):
    return self.event_name