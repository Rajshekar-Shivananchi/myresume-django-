from django.urls import path
#from . import views
from base.views import home


urlpatterns=[
 	path('',home)

]