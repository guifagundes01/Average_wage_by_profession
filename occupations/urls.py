from django.urls import path
from . import views


urlpatterns = [
    path("<str:cbo>", views.cbo_detail, name="cbo_detail"),
]