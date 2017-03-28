"""Definition for models for diagnoses app."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Diagnosis(models.Model):
    """Diagnosis model."""

    created_timestamp = models.DateTimeField(auto_now_add=True)
    from_timestamp = models.BigIntegerField()
    to_timestamp = models.BigIntegerField()
    diagnosis = models.TextField()
    patient = models.BigIntegerField()
    doctor = models.BigIntegerField()

    class Meta(object):
        ordering = ['-created_timestamp']

    def __repr__(self):
        """__repr__ override."""
        return '<Diagnosis ({}, {}, {}, {}, {}, {}, {})>'\
               .format(self.id, self.created_timestamp, self.from_timestamp, self.to_timestamp,
                       self.diagnosis, self.patient, self.doctor)

    def __str__(self):
        """__str__ override."""
        return self.__repr__()
