from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Event
from .forms import EventForm
import time
import json
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .forms import CalendarForm, ScheduleCreateForm

def schedule_index(request):
  get_token(request)
  side = {
    'list': Event.objects.all().order_by('start_date'),
  }
  return render(request, 'schedule/schedule_index.html', side)

def add_event(request):
  if request.method == "GET":
    raise Http404()

  datas = json.loads(request.body)

  eventForm = EventForm(datas)
  if eventForm.is_valid() == False:
    raise Http404()

  start_date = datas["start_date"]
  end_date = datas["end_date"]
  event_name = datas["event_name"]

  formatted_start_date = time.strftime(
    "%Y-%m-%d", time.localtime(start_date / 1000))
  formatted_end_date = time.strftime(
    "%Y-%m-%d", time.localtime(end_date / 1000))

  event = Event(
    event_name=str(event_name),
    start_date=formatted_start_date,
    end_date=formatted_end_date,
  )
  event.save()
  return redirect('schedule:schedule_index')

def get_events(request):
  if request.method == "GET":
    raise Http404()

  datas = json.loads(request.body)

  calendarForm = CalendarForm(datas)
  if calendarForm.is_valid() == False:
    raise Http404()

  start_date = datas["start_date"]
  end_date = datas["end_date"]

  formatted_start_date = time.strftime(
    "%Y-%m-%d", time.localtime(start_date / 1000))
  formatted_end_date = time.strftime(
    "%Y-%m-%d", time.localtime(end_date / 1000))

  events = Event.objects.filter(
      start_date__lt=formatted_end_date, end_date__gt=formatted_start_date
  )

  list = []
  for event in events:
      list.append(
          {
            "title": event.event_name,
            "start": event.start_date,
            "end": event.end_date,
          }
      )

  return JsonResponse(list, safe=False)

def schedule_detail(request, pk):
  content = {
    'event': get_object_or_404(Event, pk=pk)
  }
  return render(request, 'schedule/schedule_detail.html', content)


def schedule_update(request, pk):
  event = get_object_or_404(Event, pk=pk)
  form = ScheduleCreateForm(request.POST or None, instance=event)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('schedule:schedule_index')

  context = {
     'form': form
  }
  return render(request, 'schedule/schedule_update.html', context)

def schedule_delete(request, pk):
  event = get_object_or_404(Event, pk=pk)
  if request.method == 'POST':
    event.delete()
    return redirect('schedule:schedule_index')

  context = {
    'event': event
  }
  return render(request, 'schedule/schedule_confirm_delete.html', context)
