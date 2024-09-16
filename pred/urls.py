from django.contrib import admin
from django.urls import path
from pred import views

urlpatterns = [
    path('', views.pred,name='pred'),
    path('det1', views.det1,name='det1'),
    path('res1', views.res1,name='res1'),
    path('det2', views.det2,name='det2'),
    path('res2', views.res2,name='res2'),
    path('det3', views.det3,name='det3'),
    path('res3', views.res3,name='res3'),
    path('det4', views.det4,name='det4'),
    path('res4', views.res4,name='res4'),
    path('det5', views.det5,name='det5'),
    path('res5', views.res5,name='res5'),
    path('det6', views.det6,name='det6'),
    path('res6', views.res6,name='res6'),
]