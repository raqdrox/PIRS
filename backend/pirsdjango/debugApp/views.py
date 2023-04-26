from django.shortcuts import render

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from biometricApi.models import FingerprintIdMapping,PatientIdMapping
from patientapp.models import Patient,MedicalData,EmergencyContact
from userprofile.models import Profile


# Create your views here.
        



class DebugView(APIView):
    def get(self, request, *args, **kwargs):

        Patient.objects.all().delete()
        FingerprintIdMapping.objects.all().delete()
        PatientIdMapping.objects.all().delete()
        MedicalData.objects.all().delete()
        EmergencyContact.objects.all().delete()
        
        
        return Response('Debug', status=status.HTTP_200_OK)

        
