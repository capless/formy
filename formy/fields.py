from valley.mixins import *


from formy.templates.fields import base_field_template,select_field_template
from valley.properties import OrderedBaseProperty as VBaseProperty


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
        placeholder=None,
        help_text=None,
        **kwargs
    ):
        super(BaseField, self).__init__(default_value=default_value,
            required=required,
            validators=validators,
            verbose_name=verbose_name,
            **kwargs)
        self.default_value = default_value
        self.required = required
        self.kwargs = kwargs

        self.css_classes = css_classes or self.css_classes
        self.verbose_name = verbose_name
        self.placeholder = placeholder or self.verbose_name
        self.help_text = help_text
        self.validators = list()
        self.get_validators()
        self.validators = set(self.validators)

    def get_verbose_name(self):
        return self.verbose_name or self.name.replace('_',' ').title()

    def render(self,name=None,value=None,css_classes=None,input_type=None,
               placeholder=None,choices=None):
        name = name or self.name
        verbose_name = self.verbose_name or name.replace('_',' ').title()
        value = value or self.value
        choices = choices or self.choices
        input_type = input_type or self.input_type
        placeholder = placeholder or self.placeholder or verbose_name

        if css_classes and self.css_classes:
            css_classes = '{},{}'.format(self.css_classes,css_classes)
        elif not css_classes:
            css_classes = self.css_classes
        return self.template.render(
            name=name,
            choices=choices,
            value=value,
            verbose_name=verbose_name,
            placeholder=placeholder,
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


class PasswordField(CharField):
    input_type = 'password'


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


class ChoiceField(BaseField):
    template = select_field_template
