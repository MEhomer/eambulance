"""Definition for models for diagnoses app."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible
class Diagnosis(models.Model):
    """Diagnosis model."""

    created_timestamp = models.DateTimeField(default=timezone.now)
    diagnosis = models.TextField()
    doctor = models.BigIntegerField()
    diagnosis_id = models.TextField()

    # Deprecated
    patient = models.BigIntegerField(null=True)
    from_timestamp = models.BigIntegerField(null=True)
    to_timestamp = models.BigIntegerField(null=True)

    class Meta(object):
        ordering = ['-created_timestamp']

    def __repr__(self):
        """__repr__ override."""
        return '<Diagnosis ({}, {}, {}, {}, {}, {}, {}, {})>'\
               .format(self.id, self.created_timestamp, self.diagnosis_id, self.doctor, self.diagnosis,
                       self.from_timestamp, self.to_timestamp, self.patient)

    def __str__(self):
        """__str__ override."""
        return self.__repr__()
