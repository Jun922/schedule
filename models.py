from django.db import models

class Event(models.Model):
  start_date = models.DateField('予定開始日')
  end_date = models.DateField('予定終了日')
  event_name = models.CharField('タイトル', max_length=32)
  info = models.TextField('予定内容', max_length=100, blank=True)

  def __str__(self):
    return self.event_name