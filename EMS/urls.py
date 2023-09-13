from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('eventdetails/<int:pk>',views.eventdetails,name='eventdetails'),

]
