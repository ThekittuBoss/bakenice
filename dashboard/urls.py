from django.urls import path
from dashboard import views


urlpatterns = [
    path('dashbaord/',views.dashboard,name='dashbaord'),
    path('add/', views.addpost, name='add')
]
