from django.urls import path
from .views import PDFFileCreateView

urlpatterns = [
    path('upload/', PDFFileCreateView.as_view(), name='pdf-upload'),
]