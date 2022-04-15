from django.urls import path
from .views import indexView

urlpatterns = [
    path('', indexView, name='index'),
    #path('submitjson/', subitJsonView, name='submitjson'),
]