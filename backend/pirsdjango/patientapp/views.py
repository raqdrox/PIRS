from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Patient

@csrf_exempt
def fetch_records(request):
    if request.method == 'POST':
        # Get the biometric data from the Arduino
        biometric_data = request.POST.get('biometric_data')

        # Look up the patient record by biometric data
        try:
            patient = Patient.objects.get(biometric_data=biometric_data)
            data = {
                'name': patient.name,
                'age': patient.age,
                'gender': patient.gender
            }
            return JsonResponse(data)
        except Patient.DoesNotExist:
            return JsonResponse({'error': 'Patient not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
