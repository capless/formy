from valley.mixins import SlugVariableMixin, EmailVariableMixin
from valley.properties import *

from formy.templates.fields import base_field_template


class BaseFieldMixin(object):
    template = base_field_template
    css_classes = ''
    value = None
    name = None
    input_type = 'text'

    def __init__(
        self,
        default_value=None,
        required=False,
        validators=[],
        verbose_name=None,
        css_classes=None,
        **kwargs
    ):

        self.default_value = default_value
        self.required = required
        self.kwargs = kwargs
        if css_classes:
            self.css_classes = css_classes
        self.validators = list()
        self.get_validators()
        self.validators = set(self.validators)
        if verbose_name:
            self.verbose_name = verbose_name

    def render(self,name=None,value=None,css_classes=None,input_type=None):
        if not name:
            name = self.name
        if not value:
            value = self.value
        if not css_classes:
            css_classes = self.css_classes
        if not input_type:
            input_type = self.input_type

        return self.template.render(
            name=name,
            value=value,
            css_classes=css_classes,
            input_type=input_type,
        )


class CharField(BaseFieldMixin,CharProperty):
    pass

class SlugField(BaseFieldMixin,SlugVariableMixin,CharProperty):
    pass


class EmailField(BaseFieldMixin,EmailVariableMixin,CharProperty):
    input_type = 'email'


class IntegerField(BaseFieldMixin,IntegerProperty):
    input_type = 'number'


class FloatField(BaseFieldMixin, FloatProperty):
    input_type = 'number'


class BooleanField(BaseFieldMixin,BooleanProperty):
    input_type = 'checkbox'


class DateField(BaseFieldMixin, DateProperty):
    input_type = 'date'

class DateTimeField(BaseFieldMixin,DateTimeProperty):
    input_type = 'datetime-local'
