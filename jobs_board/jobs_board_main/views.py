from django.shortcuts import render

from django.http import HttpResponse


from .models import Job, Subscriber, Subscription
from .signals import new_subscriber


# Create your views here.
def get_jobs(request):
    jobs = Job.objects.all()

    return render(request, 'jobs.html', {'jobs': jobs})


def get_job(request, id):
    job = Job.objects.get(pk=id)
    return render(request, 'job.html', {'job': job})


def subscribe(request, id):
    job = Job.objects.get(pk=id)
    subscriber = Subscriber(email=request.POST['email'])
    subscriber.save()

    subscription = Subscription(user=subscriber, job=job, email=subscriber.email)
    subscription.save()

    new_subscriber.send(sender=subscription.__class__, job=job, subscriber=subscriber)

    payload = {
      'job': job,
      'email': request.POST['email']
    }
    return render(request, 'subscribed.html', {'payload': payload})
