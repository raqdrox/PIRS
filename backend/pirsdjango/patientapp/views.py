import datetime
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Patient,MedicalData,EmergencyContact,FingerprintData
from .serializers import PatientSerializer,MedicalDataSerializer,EmergencyContactSerializer,FingerprintDataSerializer
from userprofile.models import Profile
from biometricApi.models import FingerprintIdMapping
    

class PatientCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def post(self, request):
        patient, _ = Patient.objects.get_or_create(id=request.data['id'])
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save(
                last_updated_by=Profile.objects.get(user=request.user).name,
                last_updated_time=datetime.datetime.now()
                )  
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def put(self, request, *args, **kwargs):
        patient = Patient.objects.get(id=kwargs['pk'])
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save(
                    last_updated_by=Profile.objects.get(user=request.user).name,
                    last_updated_time=datetime.datetime.now()
                    )  
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientGetView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class PatientGetByNameView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def get(self, request, *args, **kwargs):
        patient = Patient.objects.filter(name=kwargs['name'])
        if patient:
            serializer = PatientSerializer(patient, many=True)
            return Response(serializer.data)
       
        return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)
    
    
class PatientFingerprintAddView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()

    def post(self, request):
        patient = Patient.objects.get(id=request.data['patient_id'])
        
        
        fingerprintIdMapping, created = FingerprintIdMapping.objects.get_or_create(id=request.data['fingerprint_store_id'])      
        if created:
            return Response('Fingerprint Store Id not found', status=status.HTTP_400_BAD_REQUEST)
        fprint,_ = FingerprintData.objects.get_or_create(patient_id=patient.id)
        fprint.fingerprint_data = fingerprintIdMapping.fingerprint
        patient.fingerprint_data = fprint
        patient.save()
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
