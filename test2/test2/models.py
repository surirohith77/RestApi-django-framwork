from django.db import models


class Cricketers(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=15)


    def __str__(self):
        return self.name


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)