from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  url(r'^generate/', views.generate),
  url(r'^startover/', views.startover)
]
