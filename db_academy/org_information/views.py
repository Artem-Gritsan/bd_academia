from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from org_information.models import Organizations
from org_information.serializers import OrgDataSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class OrgDataView(ListAPIView):

    queryset = Organizations.objects.all()
    serializer_class = OrgDataSerializer


class SingleDataView(RetrieveUpdateAPIView):

    queryset = Organizations.objects.all()
    serializer_class = OrgDataSerializer
    # permission_classes = [IsAuthenticated]