from RestApp.models import Login
from RestApp.serializers import LoginSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import YAMLParser,JSONParser
from django.http import HttpResponse
import json
import redis
myredis = redis.StrictRedis(host='localhost', port=6379, db=0)

#bairaginath 

class Register(APIView):

    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        login =Login.objects.all()
        serializer = LoginSerializer(login, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        requestData=request.DATA
        print requestData
        requestData=json.loads(json.dumps(requestData))
        try:
             serializer = LoginSerializer(requestData)
        except Exception as ex:
             print type(ex)
        if serializer.is_valid:
            jsone = JSONRenderer().render(serializer.data)
            loginModel=serializer.restore_object(serializer.data,Login())
            username=requestData['username']
            password=requestData['password']
            if(myredis.get(username)==None):
                  myredis.set(username,password)
                  loginModel.save()
                  return HttpResponse(" Registration Successfully  "+jsone)
            else:
                   return HttpResponse("Registration Failure, user already exist   "+jsone)
        else:
            return Response(serializer.errors)
