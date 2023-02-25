from django.urls import path
from . import views as v


urlpatterns = [
    path('',v.home, name = 'home'),
    path('<str:room>/', v.room, name='room'),
    path('checkview', v.checkview, name='checkview'),
    path('send', v.send, name='send'),
    path('getMessages/<str:room>/', v.getMessages, name='getMessages'),

]