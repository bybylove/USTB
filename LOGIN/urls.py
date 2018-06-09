from django.urls import path
from LOGIN.views import *
urlpatterns = [
    path('', login),
    path('logout/',logout),
    path('setting/',setting)
]