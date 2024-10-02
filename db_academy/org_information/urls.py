from django.urls import path
from org_information import views
from django.urls import include


urlpatterns = [
    path('all/', views.OrgDataView.as_view()),
    path('<int:pk>/', views.SingleDataView.as_view()),
    path('', include('djoser.urls'))
]