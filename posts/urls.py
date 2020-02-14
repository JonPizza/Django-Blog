from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('ctf/<str:ctf>/', filter_for_ctf),
    path('<str:ctf>/<int:pk>', get_post),
]