from django.urls import path
from .views import PatientCreateView , PatientUpdateView , PatientGetView , PatientGetByNameView , PatientFingerprintAddView


urlpatterns = [
    path('create/', PatientCreateView.as_view(), name='patient-create'),
    path('update/<int:pk>/', PatientUpdateView.as_view(), name='patient-update'),
    path('get/<int:pk>/', PatientGetView.as_view(), name='patient-get'),
    path('getbyname/<str:name>/', PatientGetByNameView.as_view(), name='patient-getbyname'),
    path('fingerprint/add/', PatientFingerprintAddView.as_view(), name='patient-fingerprint-add'),



    

 ]