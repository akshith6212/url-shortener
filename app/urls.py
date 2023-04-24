from django.urls import path
from . import views

urlpatterns = [
  path('',views.index, name="homepage"),
  path('<str:id>/', views.shortenurl, name="shortenurl")
]
