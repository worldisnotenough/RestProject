from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from rest_framework.renderers import JSONRenderer
from RestApp.serializers import LoginSerializer
from RestApp.models import Author
from django.core.context_processors import csrf

def index_view(request):
    """
Ensure the user can only see their own profiles.
"""
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)

#bairaginath behera


from rest_framework.response import Response

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
import redis
myredis = redis.StrictRedis(host='localhost', port=6379, db=0)
@csrf_exempt

@api_view(['POST'])
def login(request):
    if request.method=='POST' :
        # body=request.body
        # bodyData=eval(body)
        requestData=request.DATA
        requestData=json.loads(json.dumps(requestData))
        try:
             serializer = LoginSerializer(requestData)
        except Exception as ex:
             print type(ex)



        if serializer.is_valid:
            jsone = JSONRenderer().render(serializer.data)
            jsonData=json.loads(jsone)
            username=jsonData['username']
            password=jsonData['password']
            if (password==myredis.get(username)):
                  return HttpResponse("Login Successfully"+jsone)
            else :
                  return HttpResponse("login Failure"+jsone)
