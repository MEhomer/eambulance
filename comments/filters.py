"""Filter classes for the models from models.py."""
from utils import filters

from .models import Comment


class CommentFilter(filters.Filter):
    """Comment filter."""

    from_timestamp = filters.IntegerField({None: 'from_timestamp',
                                           'lt': 'from_timestamp__lt',
                                           'lte': 'from_timestamp__lte',
                                           'gt': 'from_timestamp__gt',
                                           'gte': 'from_timestamp__gte'})
    to_timestamp = filters.IntegerField({None: 'to_timestamp',
                                         'lt': 'to_timestamp__lt',
                                         'lte': 'to_timestamp__lte',
                                         'gt': 'to_timestamp__gt',
                                         'gte': 'to_timestamp__gte'})
    patient = filters.IntegerField({None: 'patient'})

    def _get_objects(self, filters):
        """Get all objects."""
        return Comment.objects.filter(**filters)
