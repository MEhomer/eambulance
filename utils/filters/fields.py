"""Field base classes and derived classes."""
import re


class Field(object):
    """Base Field class from which all other Field classes must inherit."""

    def __init__(self, filters=None):
        """Initialize a field."""
        if filters is None:
            filters = {}

        self.filters = filters
        self.parser = re.compile(r'((?P<filter>.*?):)?(?P<value>.*)')

    def validate(self, query):
        """Basic implementation of `validate`."""
        match = self.parser.match(query)

        if match is None:
            return {'success': False, 'reason': 'No query matched'}

        filter_ = match.groupdict()['filter']
        value_ = match.groupdict()['value']

        return self._validate(filter_, value_)

    def _validate(self, filter_, value_):
        """Validate the `filter_` and the `value_`."""
        if value_ is None:
            return {'success': False, 'reason': 'No valid value parsed'}
        elif filter_ not in self.filters:
            return {'success': False, 'reason': 'No valid filter parsed'}

        return {'success': True, 'filter': {self.filters[filter_]: value_}}


class IntegerField(Field):
    """Integer Field."""

    def _validate(self, filter_, value_):
        if value_ is None:
            return {'success': False, 'reason': 'No valid value parsed'}
        elif filter_ not in self.filters:
            return {'success': False, 'reason': 'No valid filter parsed'}

        try:
            value_ = int(value_)
        except ValueError:
            return {'success': False, 'reason': 'Value is not of type integer'}

        return {'success': True, 'filter': (self.filters[filter_], value_)}
