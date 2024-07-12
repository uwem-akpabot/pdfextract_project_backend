from djongo import models

class PDFFile(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    content = models.TextField(blank=True)
    nouns = models.JSONField(default=list)
    verbs = models.JSONField(default=list)
    email = models.EmailField(unique=True, blank=True, null=True)