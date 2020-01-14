from django.core import validators
from django.db import models
from teryt_tree.models import JednostkaAdministracyjna

from ..generic.models import TimestampUserLogModel
from ..generic.validators import ExactLengthsValidator


class AddressData(models.Model):
    email = models.EmailField()
    city = models.CharField(max_length=100)
    epuap = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    voivodeship = models.CharField(max_length=100)
    flat_no = models.CharField(max_length=100, null=True, blank=True)


class ExternalIdentifier(models.Model):

    nip = models.CharField(
        max_length=10,
        validators=[ExactLengthsValidator([10]), validators.RegexValidator("[0-9]*$"),],
    )

    regon = models.CharField(
        max_length=14,
        validators=[
            ExactLengthsValidator([10, 14]),
            validators.RegexValidator("[0-9]*$"),
        ],
    )


class Institution(TimestampUserLogModel):
    name = models.CharField(max_length=256)

    administrative_unit = models.OneToOneField(
        to=JednostkaAdministracyjna, on_delete=models.CASCADE, null=True, blank=True
    )
    address = models.OneToOneField(
        AddressData, on_delete=models.CASCADE, null=True, blank=True
    )
    external_identifier = models.OneToOneField(
        ExternalIdentifier, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.pk})"
