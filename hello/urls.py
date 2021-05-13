from django.urls import path

from . import views

urlpatterns=[
  path("",views.index,name="index"),
  path("<int:num>",views.number_plus_five,name="number_plus_five"),
  path("rohit",views.rohit,name="rohit"),
  path("atul",views.atul,name="atul"),
  path("<str:name>",views.greet,name="greet"),
]