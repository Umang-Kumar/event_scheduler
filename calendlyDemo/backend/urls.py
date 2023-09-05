from django.urls import path
from . import views

app_name = 'backend'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('create/', views.CreateEventView.as_view(), name='create'),
    path('event/<str:link>/', views.EventDetailView.as_view(), name='event-detail'),
    path('event/<str:link>/booked-slots/', views.EventBookedSlotsView.as_view(), name='event-booked-slots'),
]