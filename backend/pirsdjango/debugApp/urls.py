from django.urls import path

from .views import DebugView

urlpatterns = [
    path('', DebugView.as_view(), name='debug'),
]
