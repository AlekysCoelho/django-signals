from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    """
    Model representing a person and makes a OneToOneField relationship
    with Django's default User, containing basic information
    such as email, phone number and slug.
    """

    person = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, related_name="persons"
    )
    first_name = models.CharField(_("First name"), max_length=150)
    email = models.EmailField(_("email address"), max_length=100, unique=True)
    phone_number = models.CharField(_("Phone number"), max_length=20)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self) -> None:
        return f"{self.person.username}"


class Historical(models.Model):
    """History of personal information."""

    first_name = models.CharField(_("First name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    username = models.CharField(_("username"), max_length=150)
    email = models.EmailField(_("email address"), max_length=100)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __str__(self) -> None:
        return f"{self.username}"
