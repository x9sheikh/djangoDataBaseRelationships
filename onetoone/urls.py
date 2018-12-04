from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.onetoone, name='onetoone'),
    path('detail/<int:college_id>/', views.detail, name='detail')

]
