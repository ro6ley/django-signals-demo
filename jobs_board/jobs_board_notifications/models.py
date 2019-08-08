from django.db import models
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

from jobs_board_main.signals import new_subscriber
from jobs_board_main.models import Job, Subscriber, Subscription


@receiver(new_subscriber, sender=Subscription)
def handle_new_subscription(sender, **kwargs):
    subscriber = kwargs['subscriber']
    job = kwargs['job']

    message = """User {} has just subscribed to the Job {}.
    """.format(subscriber.email, job.title)

    print("\n**************************************\n")
    print(message)
    print("\n**************************************\n")



@receiver(pre_delete, sender=Job)
def handle_deleted_job_posting(**kwargs):
    job = kwargs['instance']

    # find the subscribers list
    subscribers = Subscription.objects.filter(job=job)

    for subscriber in subscribers:
        message = """Dear {}, the job posting {} by {} has been taken down.
        """.format(subscriber.email, job.title, job.company)

        print("\n**************************************\n")
        print(message)
        print("\n**************************************\n")
