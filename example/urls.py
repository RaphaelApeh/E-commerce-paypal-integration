from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='example'),
    path('test/',views.example,name='test')
]
