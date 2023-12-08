from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sanction
from .serializers import SanctionSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/sanction/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/sanction/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/sanction/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/sanction/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/sanction/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getSanctions(request):
    sanctions = Sanction.objects.all()
    serializer = SanctionSerializer(sanctions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSanctionID(request, pk):
    sanctions = Sanction.objects.get(id=pk)
    serializer = SanctionSerializer(sanctions, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateSanction(request, pk):
     data = request.data
     sanction = Sanction.objects.get(id=pk)
     serializer = SanctionSerializer(instance=sanction, data=data)

     if serializer.is_valid():
         serializer.save()

     return Response(serializer.data)