from django.urls import path 
from .views import one , persons , person , create_person

app_name = 'home'
urlpatterns = [
    path('one/', one , name='one' ),
    path('persons/', persons ),
    path('person/<int:id>', person  ),
    path('create_person/', create_person  ),
]
