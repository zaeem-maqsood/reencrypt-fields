from django.core.management.base import BaseCommand
from django import apps
from django.db import transaction

from django_cryptography.fields import EncryptedMixin


def re_encrypt_fields_in_model(model, field):
    """
    Save the data from each object into a temp variable and
    write it back encrypted with the new key.

    Using bulk update instead of save() method to avoid
    running signals, essentially copying the data exactly.
    """
    temp_data = None
    model_instances = model.objects.all()
    for instance in model_instances:
        temp_data = getattr(instance, field, None)
        setattr(instance, field, temp_data)
    model.objects.bulk_update(model_instances, [field])


class Command(BaseCommand):
    help = "Re-Encrypt All The Encrypted Field Data With The Current Secret Key"

    def handle(self, *args, **options):
        """
        Loop through each model in each app looking for Encrypted fields.
        Everything is in 1 transaction to rollback on any point of failure.
        """

        try:
            with transaction.atomic():
                models = apps.apps.get_models()
                for model in models:
                    fields = model._meta.get_fields()
                    for field in fields:
                        if isinstance(field, EncryptedMixin):
                            re_encrypt_fields_in_model(model, field.name)

                print("\n\n === DATA RE-ENCRYPTED SUCCESSFULLY === \n\n")

        except Exception as e:
            print(e)
            print("\n\n!!! ==== DATA HAS NOT BEEN RE-ENCRYPTED === !!!\n\n")
