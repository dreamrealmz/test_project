from django.urls import path
from .views import MeetApiView, StoresApiView

urlpatterns = [
    path('api/v1/meet/<phone_number>', MeetApiView.as_view()),
    path('api/v1/stores/<phone_number>', StoresApiView.as_view()),
]
