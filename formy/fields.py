from valley.mixins import *


from formy.templates.fields import base_field_template
from valley.properties import BaseProperty as VBaseProperty


class BaseField(VBaseProperty):
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


class CharField(CharVariableMixin,BaseField):
    pass


class SlugField(SlugVariableMixin,BaseField):
    pass


class EmailField(EmailVariableMixin,BaseField):
    input_type = 'email'


class IntegerField(IntegerVariableMixin,BaseField):
    input_type = 'number'


class FloatField(FloatVariableMixin, BaseField):
    input_type = 'number'


class BooleanField(BooleanMixin,BaseField):
    input_type = 'checkbox'


class DateField(DateMixin, BaseField):
    input_type = 'date'

    def __init__(
            self,
            default_value=None,
            required=True,
            validators=[],
            verbose_name=None,
            auto_now=False,
            auto_now_add=False,
            **kwargs):

        super(
            DateField,
            self).__init__(
            default_value=default_value,
            required=required,
            validators=validators,
            verbose_name=verbose_name,
            **kwargs)
        self.auto_now = auto_now
        self.auto_now_add = auto_now_add


class DateTimeField(DateTimeMixin,BaseField):
    input_type = 'datetime-local'

    def __init__(
            self,
            default_value=None,
            required=True,
            validators=[],
            verbose_name=None,
            auto_now=False,
            auto_now_add=False,
            **kwargs):

        super(
            DateTimeField,
            self).__init__(
            default_value=default_value,
            required=required,
            validators=validators,
            verbose_name=verbose_name,
            **kwargs)
        self.auto_now = auto_now
        self.auto_now_add = auto_now_add
