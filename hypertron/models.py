from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.TextField(null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    city = models.TextField(null=False, blank=False)
    state = models.TextField(null=False, blank=False)
    zip = models.TextField(null=False, blank=False)
    country = models.TextField(null=False, blank=False)
    latitude = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=7)
    longitude = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=7)
    contact = models.ForeignKey('ContactPerson', on_delete=models.PROTECT, null=True, blank=True)

class Show(models.Model):
    venue = models.ForeignKey('Venue', on_delete=models.PROTECT, null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    frequency = models.IntegerField(null=False, blank=False)

class Second(models.Model):
    class Meta:
        unique_together = ('show', 'second')

    show = models.ForeignKey('Show', on_delete=models.CASCADE, null=False, blank=False)
    second = models.IntegerField(null=False, blank=False)

class Pixel(models.Model):
    venue = models.ForeignKey('Venue', on_delete=models.PROTECT, null=False, blank=False)
    row = models.IntegerField(null=False, blank=False)
    seat = models.IntegerField(null=False, blank=False)
    section = models.CharField(null=False, blank=False, max_length=2)

class SecondPixel(models.Model):
    class Meta:
        unique_together = ('pixel','second')

    pixel = models.ForeignKey('Pixel', on_delete=models.PROTECT, null=False, blank=False)
    second = models.ForeignKey('Second', on_delete=models.CASCADE, null=False, blank=False)
    state = models.TextField(null=False, blank=False)

class ContactPerson(models.Model):
    firstName = models.TextField(null=False, blank=False)
    lastName = models.TextField(null=False, blank=False)
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
