from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()

router.register('post',views.PostView)

urlpatterns = [

    path('',include(router.urls)),

]