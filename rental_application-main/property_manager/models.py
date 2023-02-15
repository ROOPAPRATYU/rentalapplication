from django.db import models


# Create your models here.
class Property(models.Model):
    property_name = models.CharField(max_length=200, default=None, null=True)
    tenant_name = models.CharField(max_length=200, default=None, null=True)
    property_age = models.IntegerField(default=None, null=True)
    rent_amount = models.CharField(max_length=12, default=None, null=True)
    rent_date = models.DateField(default=None, null=True)
    adhar_number = models.CharField(max_length=2, default=None, null=True)
    adhar_image = models.ImageField(upload_to="adhar_pic", default=None, null=True)
    property_image = models.ImageField(
        upload_to="property_image", default=None, null=True
    )
    create_date = models.DateField(auto_now_add=True)
