from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('stats/', views.pageview_stats, name='pageview_stats'),
]
