from post.models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver
from post.ml_utils import fake_or_not


@receiver(post_save, sender=Post)
def fake_or_truth(sender, instance, **kwargs):
    print("signal called")
    print(instance.fake)
    instance.fake = fake_or_not(instance.content)
    instance.save()
