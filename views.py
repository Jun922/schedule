from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def schedule_list(request):
  template = loader.get_template("schedule/schedule_list.html")
  return HttpResponse(template.render())