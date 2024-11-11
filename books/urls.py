from django.urls import path
from . import views as v


urlpatterns = [
    path("", v.index),
    path("services/", v.services),
    path("about/", v.about),
    path("contact/", v.contact),
    path("fligth/", v.fligth),
     path("travel/", v.travel),
    path("hotel/", v.hotel),
    path("fligthbook/", v.fligthbook),
    path("hotel1/", v.hotel1),
    path("travel1/", v.travel1),
    path("wow/", v.wow),
    path("explore/", v.explore),
]