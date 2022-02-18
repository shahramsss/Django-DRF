
from rest_framework import viewsets
from . models import Person
from .serializers import PersonSerilizer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class PersonViewset(viewsets.ModelViewSet):
# class PersonViewset(viewsets.ViewSet):
        queryset = Person.objects.all()
        serializer_class = PersonSerilizer

    # def list (self , request ):
    #     queryset = Person.objects.all()
    #     serializer = PersonSerilizer(queryset , many = True)
    #     return Response(serializer.data)

    # def retrieve(self , request , pk=None):
        
    #     queryset = Person.objects.all()
    #     person = get_object_or_404(queryset , pk = pk)
    #     serializer = PersonSerilizer(person)
    #     return Response(serializer.data)

    # def create (self , request):
    #     seriaizer = PersonSerilizer(data = request.data )
    #     if seriaizer.is_valid():
    #         seriaizer.save()
    #         return Response({'message':'ok'})
    #     else:
    #         return Response(seriaizer.errors)
