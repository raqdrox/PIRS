from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FingerprintIdMapping,PatientIdMapping
from .serializers import FingerprintIdMappingSerializer,PatientIdMappingSerializer
from patientapp.models import Patient#,FingerprintData
from patientapp.serializers import PatientSerializer


# Create your views here.
'''
class FingerprintDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = FingerprintData.objects.all()

    def get(self, request):
        fpList= self.queryset.values_list('patient_id','fingerprint_data')
        if fpList:
            #convert tuple list to key value pair
            fpList = [dict(zip(['patient_id','fingerprint_data'], row)) for row in fpList]


            #fplist to dict
            fpdict= dict(enumerate(fpList))
            print(fpdict)
            return Response(fpList)
        

        return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)
    
'''
class FingerprintStoreView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = FingerprintIdMapping.objects.all()
    serializer_class = FingerprintIdMappingSerializer

    def get(self, request):
        fingerprint_id_mapping = self.queryset.all()
        if fingerprint_id_mapping:
            serializer = self.serializer_class(fingerprint_id_mapping, many=True)
            return Response(serializer.data)
        return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FingerprintGetAvailableIDView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientIdMapping.objects.all()
    serializer_class = PatientIdMappingSerializer

    def get(self, request):
        data=self.queryset.values_list('finger_id',flat=True)

        print("data: ",data)


        #get next available finger_id from db including gaps
        data=list(data)
        data.sort()
        foundid=-1

        #find first gap
        for i in range(len(data)):
            print("i: ",i,"data[i]: ",data[i],"i!=data[i]: ",i!=data[i],"foundid: ",foundid)
            if data[i]!=i:
                foundid=i
                break
        if foundid==-1:
            foundid=len(data)
        



        serializer = PatientIdMappingSerializer(data={'finger_id':foundid,'patient_id':-1})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.get('finger_id'))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PatientByFingerprintIDView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientIdMapping.objects.all()
    serializer_class = PatientIdMappingSerializer

    def get(self, request, *args, **kwargs):
        patient_id_mapping,created= PatientIdMapping.objects.get_or_create(finger_id=kwargs['finger_id'])

        if not created:
            patient = Patient.objects.get(id=patient_id_mapping.patient_id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
            
    
        return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)
        

class ClearUnusedPatientIdMapping(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientIdMapping.objects.all()
    serializer_class = PatientIdMappingSerializer

    def get(self, request):
        #clear all objects from db where patient_id is -1

        self.queryset.filter(patient_id=-1).delete()




        

        
        
        return Response('Done', status=status.HTTP_200_OK)

