from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


def validate_zipcode(value, length=5):
    if len(str(value)) != length:
        raise ValidationError("zip code length should be {}".format(length))
    if not value.isdigit():
        raise ValidationError("zip code should only contain numbers")


class PropertyData(models.Model):
    email = models.EmailField(max_length=200)
    property_address = models.CharField(max_length=300)
    zip_code = models.CharField(validators=[validate_zipcode], max_length=5)
    number_bedrooms = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    number_bathrooms = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    square_footage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)])


class QuoteRecord(models.Model):
    property_data = models.ForeignKey(PropertyData, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    monthly_estimate = models.PositiveIntegerField(validators=[MaxValueValidator(100000000)])

