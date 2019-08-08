from django.dispatch import Signal


new_subscriber = Signal(providing_args=["job", "subscriber"])
