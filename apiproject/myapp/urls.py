from django.urls import include,    path
from rest_framework.routers import DefaultRouter
from  .views import Itemviewsets

router=DefaultRouter()
router.register(r'items',Itemviewsets)

urlpatterns=[
    path('',include(router.urls))
]