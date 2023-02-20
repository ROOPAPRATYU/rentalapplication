from django.shortcuts import render

# Create your views here.

from twilio.rest import Client
import schedule
import datetime

from rest_framework import request
from rest_framework.decorators import permission_classes,api_view
from rental_application.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpResponse
from propertyManager.models import PropertyDetail
from propertyManager.serializers import ProperySerializer
from rest_framework.permissions import IsAuthenticated
#from django.views.decorators.csrf import csrf_protect
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
  
# Create your views here.
def send_notification(request:Request):
    #collect ("email","rent_date","rent","phone_number") data from the propertydetails database table
    tenentdetails=PropertyDetail.objects.values_list("email","rent_date","rent","phone_number","tenant_name","property_name","bhk")
    for userinfo in tenentdetails:
        timing=datetime.datetime.today()
        
        #default date considered as 3rd of every month and compared 
        if timing.day==20:
            
            print(userinfo[3])
            message = client.messages.create(from_='whatsapp:+14155238886',body='Hi {} please pay your rent amount {} for property {}({}BHK) ,your rent on due please pay before {}/{}/{},if already paid please ignore it'.format(userinfo[4],userinfo[2],userinfo[5],userinfo[6],timing.day,timing.month,timing.year),to='whatsapp:+91{}'.format(userinfo[3]))
            print(message.body)
            print(message.sid)
        else:
            print("no due date to send it")
    
    return HttpResponse('Great! Expect a message on whatsapp..')




    

