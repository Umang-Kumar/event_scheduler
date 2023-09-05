from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class EventCreation(models.Model):

    class Meta:
        verbose_name = 'Event Creation'
        verbose_name_plural = 'Event Creations'
        ordering = ['id']


    title = models.CharField(max_length=200, blank=False, null=False)
    type = models.CharField(max_length=200)
    description = RichTextField(max_length=500)
    location = models.CharField(max_length=200)
    prefered_date_time = models.DateTimeField(default=None, null=True, blank=True)
    time_alloted = models.IntegerField(default=0)
    link = models.SlugField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    total_slots = models.IntegerField(default=0)
    booked_slots = models.IntegerField(default=0)

    def get_booked_slots(self):
        return BookedSlot.objects.filter(event=self)

    def is_slot_booked(self, start_time, end_time):
        return BookedSlot.objects.filter(
            event=self,
            start_time__lte=end_time,
            end_time__gte=start_time,
        ).exists()

    def available_slots(self):
        return self.total_slots - self.booked_slots

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = slugify(self.title)
        super(EventCreation, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/admin/{self.link}"


class BookedSlot(models.Model):
    event = models.ForeignKey(EventCreation, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Booked Slot for {self.event.title} ({self.start_time} - {self.end_time})"

