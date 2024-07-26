from django.db import models


class Cricketers(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class AllUsers(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
