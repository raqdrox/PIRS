from django.urls import path
from .views import FingerprintDataView, FingerprintStoreView




urlpatterns = [
    path('fingerprints/', FingerprintDataView.as_view(), name='fingerprint-fetch'),
    path('fingerprints/store/', FingerprintStoreView.as_view(), name='fingerprint-store'),


 ]