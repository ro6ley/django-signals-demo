from django.db.models.signals import post_delete
from django.dispatch import receiver

from jobs_board.jobs_board_main.signals import new_subscriber
from jobs_board.jobs_board_main.models import Job, Subscriber, Subscription


# new_subscriber.connect(handle_new_subscription)


@receiver(new_subscriber, sender=Subscription)
def handle_new_subscription(sender, **kwargs):
    print(kwargs)
    print("\n\n**************************************\nP1NG\n\n**************************************")


@receiver(post_delete, sender=Job)
def handle_deleted_job_posting(**kwargs):
    print(kwargs)
    print("\n\n**************************************\nP0NG\n\n**************************************")
