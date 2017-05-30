from __future__ import unicode_literals

from django.db import models


class ScheduleManager(models.Manager):

    def make_appointment(self, *args):
        errormsg =[]
        status = True
        if args[0] < 0:
            error.msg.append('date cannot be empty')
            status = False
        else:
            Schedule.objects.create(date= args[0], time=args[1])




# Create your models here.
class Schedule(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ScheduleManager()
