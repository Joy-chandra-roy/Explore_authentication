from django.urls import path
from myApp.views import home,delItem,upItem,sinup,sinUpF,LoginF

urlpatterns = [
    path('',home,name='h'),
    path('Sinup/',sinup,name='sin'),
    path('SinForm/',sinUpF,name='sinF'),
    path('LogForm/',LoginF,name='LogF'),
    path('Delete/<int:pk>',delItem, name="dItem"),
    path('Update/<int:pk>',upItem, name="uItem"),
]
