from django.contrib import admin

from .models import Job, Subscriber, Subscription


# Register your models here.
admin.site.register(Job)
admin.site.register(Subscriber)
admin.site.register(Subscription)
