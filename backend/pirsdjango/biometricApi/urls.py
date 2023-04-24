from django.urls import path
from .views import FingerprintStoreView, FingerprintGetAvailableIDView,PatientByFingerprintIDView,ClearUnusedPatientIdMapping,DebugView




urlpatterns = [
    #path('fingerprints/', FingerprintDataView.as_view(), name='fingerprint-fetch'),
    path('fingerprints/store/', FingerprintStoreView.as_view(), name='fingerprint-store'),
    path('fingerprints/getavailableid/', FingerprintGetAvailableIDView.as_view(), name='fingerprint-getavailableid'),
    path('fingerprints/getpatientfromfid/<int:finger_id>/', PatientByFingerprintIDView.as_view(), name='fingerprint-getpatient'),
    path('fingerprints/clearunused/', ClearUnusedPatientIdMapping.as_view(), name='fingerprint-clearunused'),
    path('fingerprints/debug/', DebugView.as_view(), name='fingerprint-debug'),




 ]