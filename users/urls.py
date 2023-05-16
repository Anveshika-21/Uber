from django.urls import path,include
from  .views import *


from users.urls import *


urlpatterns=[
    path('get-all-students',GetStudentsView.as_view(),name=''),
]


