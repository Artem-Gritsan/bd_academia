from django.urls import path
from org_information import views


urlpatterns = [
    path('orgdata/', views.OrgDataView.as_view()),
]