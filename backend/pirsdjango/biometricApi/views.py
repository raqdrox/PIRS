from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FingerprintIdMapping
from .serializers import FingerprintIdMappingSerializer
from patientapp.models import Patient,FingerprintData


# Create your views here.

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

