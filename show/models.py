from django.db import models
import datetime

# Create your models here.

current_time = datetime.datetime.now()

class Grid(models.Model):

	name = models.TextField(null=False, blank=False)
	total_rows = models.IntegerField(null=False, blank=False)
	seats_per_row = models.IntegerField(null=False, blank=False)


class Pixel(models.Model):

    row = models.IntegerField(null=False, blank=False)
    seat = models.IntegerField(null=False, blank=False)    
    grid = models.ForeignKey(Grid, null=False, blank=False)


class Show(models.Model):

	name = models.TextField(null=False, blank=False)


class Frame(models.Model):

    frequency_value = models.IntegerField(null=False, blank=False)
    time = models.FloatField(null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)
    show = models.ForeignKey(Show, null=False, blank=False)


class FramePixel(models.Model):
   
    class Meta:
        unique_together = (('pixel', 'frame'),)

    pixel = models.ForeignKey(Pixel, null=False, blank=False)
    frame = models.ForeignKey(Frame, null=False, blank=False)
    action = models.TextField(null=False, blank=False)