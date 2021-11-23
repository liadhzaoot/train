from django.urls import path,include
from coach_app.views import coach_list

urlpatterns = [
    path('list/', coach_list,name='coach_list')
]