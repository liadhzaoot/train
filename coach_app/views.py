from django.shortcuts import render
from coach_app.models import CoachDB
from django.http import JsonResponse

# Create your views here.
def coach_list(request):
    coaches = CoachDB.objects.all()
    data = {
        'coaches': list(coaches.values())
    }
    return JsonResponse(data)