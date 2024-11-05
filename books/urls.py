from django.urls import path
from . import views as v


urlpatterns = [
    path("", v.index),
    path("services/", v.services),
    path("about/", v.about),
    path("contact/", v.contact),
    path("fligth/", v.fligth),
    path("fligth1/", v.fligth1),
   
    
]