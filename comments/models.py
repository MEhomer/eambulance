"""Definition of models for comments app."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible
class Comment(models.Model):
    """Comment model."""

    created_timestamp = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    comment_id = models.TextField()

    # Deprecated
    patient = models.BigIntegerField(null=True)
    from_timestamp = models.BigIntegerField(null=True)
    to_timestamp = models.BigIntegerField(null=True)

    class Meta(object):
        ordering = ['-created_timestamp']

    def __repr__(self):
        """__repr__ override."""
        return '<Comment ({}, {}, {}, {}, {}, {}, {})>'\
               .format(self.id, self.created_timestamp, self.comment_id, self.comment, self.from_timestamp,
                       self.to_timestamp, self.patient)

    def __str__(self):
        """__str__ override."""
        return self.__repr__()
