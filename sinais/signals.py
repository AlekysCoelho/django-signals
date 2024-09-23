from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Historical, Person


@receiver(pre_save, sender=Person)
def add_slug(sender, instance, **kwargs):
    """Add a slugflied to a Person instance."""

    if not instance.slug:
        instance.slug = slugify(f"{instance.person.username}-{instance.first_name}")


@receiver(post_save, sender=User)
def save_changes_user_to_person(sender, instance, created, **kwargs):
    """
    Reflects changes made directly in the User model to
    the Person model in the first_name and username fields.
    """

    if not created:
        try:
            person_instance = instance.persons
            person_instance.first_name = instance.first_name
            person_instance.last_name = instance.last_name
            person_instance.username = instance.username
            person_instance.save()
        except Person.DoesNotExist:
            pass


@receiver(post_save, sender=Person)
def save_history(sender, instance, created, **kwargs):
    """
    When a Person instance is saved in the database
    a History for that instance will be created and saved in the database.
    """

    Historical.objects.create(
        first_name=instance.first_name,
        last_name=instance.person.last_name,
        username=instance.person.username,
        email=instance.email,
        slug=instance.slug,
        person=instance,
    )
