"""Filter base classes."""
import abc


from fields import Field


class FilterMetaclass(type):
    """This metaclass sets a dictionary named `_declared_fields` on the class."""

    @classmethod
    def _get_declared_fields(cls, bases, attrs):
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, Field)]

        # If this class is subclassing another Serializer, add that Serializer's
        # fields.  Note that we loop over the bases in *reverse*. This is necessary
        # in order to maintain the correct order of fields.
        for base in reversed(bases):
            if hasattr(base, '_declared_fields'):
                fields = list(base._declared_fields.items()) + fields

        return dict(fields)

    def __new__(cls, name, bases, attrs):
        """Overload __new__."""
        attrs['_declared_fields'] = cls._get_declared_fields(bases, attrs)
        return super(FilterMetaclass, cls).__new__(cls, name, bases, attrs)


class Filter(object):
    """Base Filter class from which all other Filter classes must inherit."""

    __metaclass__ = FilterMetaclass

    def __init__(self, query_params):
        """Initialize a filter with query parameters from the request."""
        if query_params is None:
            query_params = {}

        self.query_params = query_params

        self.data = None
        self.errors = None

    def is_valid(self):
        """Check if the query parameters are valid."""
        _filters = []
        _errors = []

        for field_name, field_validator in self._declared_fields.iteritems():
            if field_name in self.query_params:
                result = field_validator.validate(self.query_params[field_name])

                if result['success'] is False:
                    _errors.append({field_name: result['reason']})
                elif result['success'] is True:
                    _filters.append(result['filter'])

        if len(_errors) > 0:
            self.errors = _errors
            self.filters = None

            return False
        else:
            self.errors = None
            self.filters = dict([(_filter, _value) for _filter, _value in _filters])

            return True

    def objects(self):
        """Return all objects."""
        return self._get_objects(self.filters)

    @abc.abstractmethod
    def _get_objects(self, filters):
        """Get all objects."""
        pass
