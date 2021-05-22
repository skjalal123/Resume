from django.urls import path
from . import views


urlpatterns = [
    path("Resume/<int:id>",views.Detail.as_view(),name="detail"),
]