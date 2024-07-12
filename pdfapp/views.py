from rest_framework import generics
from .models import PDFFile
from .serializers import PDFFileSerializer
from .utils import extract_and_process_pdf

class PDFFileCreateView(generics.CreateAPIView):
    queryset = PDFFile.objects.all()
    serializer_class = PDFFileSerializer

    def perform_create(self, serializer):
        pdf_instance = serializer.save()
        extract_and_process_pdf(pdf_instance.pdf.path, pdf_instance)
