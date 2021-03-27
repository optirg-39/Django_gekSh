from django.shortcuts import path
from . import views
urlpatterns=[
    path('el/',views.students_info),


]