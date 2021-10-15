
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views


urlpatterns = [

    path('',views.homepage,name='homepage'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('update/<str:pk>',views.update,name='update'),
    path('taskview/<str:pk>',views.details,name='details')
]