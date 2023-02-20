from django.urls import path
from. views import send_notification

urlpatterns = [
    path('sendmessage/', send_notification,name="sendnotification"),]