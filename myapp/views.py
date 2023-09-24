from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def home(request):
    return HttpResponse("Hello khalid jamal, wellcome to my website.")


class Test(APIView):

    def get(self,request):
        return Response({
            'name':'irfan ali',
            'age':25
        })
