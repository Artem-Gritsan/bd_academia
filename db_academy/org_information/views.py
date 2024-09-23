from django.shortcuts import render
from rest_framework.generics import ListAPIView
from org_information.models import Organizations
from org_information.serializers import OrgDataSerializer
# Create your views here.

class OrgDataView(ListAPIView):

    queryset = Organizations.objects.all()
    serializer_class = OrgDataSerializer