from rest_framework import serializers
from .models import PDFFile
from rest_framework.validators import UniqueValidator

class PDFFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFFile
        fields = ['id', 'title', 'pdf', 'content', 'nouns', 'verbs', 'email']
        extra_kwargs = {
            'email': {'validators': [UniqueValidator(queryset=PDFFile.objects.all())]}
        }