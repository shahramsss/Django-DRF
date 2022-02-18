
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .models import Person
from .serializers import PersonSerilizer
from rest_framework.permissions import AllowAny



@api_view(['GET', 'POST'])
def one(request):
    if request.method == 'POST':
        data = request.data['name']
        return Response({'name': data} ,  status=status.HTTP_200_OK)
    else:
        return Response({'name': 'sss'} ,  status=status.HTTP_200_OK)


@api_view()
def persons(request):
    persons = Person.objects.all()
    ser_data = PersonSerilizer(persons, many=True)
    return Response(ser_data.data , status=status.HTTP_200_OK)


@api_view()
@permission_classes([AllowAny])
def person(request, id):
    try:
        person = Person.objects.get(id=id)

    except Person.DoesNotExist:
        return Response({'erorr': 'this user is not exists'},  status=status.HTTP_400_BAD_REQUEST)
    ser_data = PersonSerilizer(person)
    return Response(ser_data.data ,  status=status.HTTP_200_OK)


@api_view(['POST'])
def create_person(requeset):
    info = PersonSerilizer(data=requeset.data)
    if info.is_valid():
        # Person(name=info.validated_data['name'], age=info.validated_data['age'],
        #        email=info.validated_data['email']).save()
        info.save()
        return Response({'message': 'ok'} ,  status=status.HTTP_200_OK)
    else:
        return Response(info.errors ,  status=status.HTTP_400_BAD_REQUEST)
