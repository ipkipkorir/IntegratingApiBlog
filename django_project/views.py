from django.shortcuts import render
import requests

def index(request):
  r1 = requests.get('https://api.reliefweb.int/v1/reports')
  data = r1.json()
  reports = data[0]['title']
  
  return render(request, 'templates/index.html', {'events': events, 'activity': activity, 'dog': dog})
