from six import with_metaclass
from valley.declarative import DeclaredVars as DV, \
    DeclarativeVariablesMetaclass as DVM
from valley.utils import import_util
from .fields import BaseField


BUILTIN_DOC_ATTRS = ('_id', '_doc_type')


class DeclaredVars(DV):
    base_field_class = BaseField
    base_field_type = '_base_fields'


class DeclarativeVariablesMetaclass(DVM):
    declared_vars_class = DeclaredVars


class BaseForm(object):
    """
    Base class for all Formy form classes.
    """
    template = 'formy.templates.base_template'

    def __init__(self, **kwargs):
        self.form_data = self.process_form_kwargs(kwargs)

    def __repr__(self):
        return '<{class_name}: {uni} >'.format(
            class_name=self.__class__.__name__, uni=self.__unicode__())

    def __unicode__(self):
        return '({0})'.format(self.__class__.__name__)

    def __iter__(self):
        for k, field in self._base_fields.items():
            field.name = k
            field.value = self.form_data.get(k)
            yield field

    def process_form_kwargs(self, kwargs):
        doc = {}
        for key, prop in list(self._base_fields.items()):
            try:
                value = prop.get_python_value(kwargs.get(key) or prop.get_default_value())
            except ValueError:
                value = kwargs.get(key) or prop.get_default_value()

            doc[key] = value
        for i in BUILTIN_DOC_ATTRS:
            if kwargs.get(i):
                doc[i] = kwargs[i]
        return doc

    def render(self,include_submit=True):
        template = import_util(self.template)
        return template.render(form=self,include_submit=include_submit)

    def validate(self):
        for k,v in self._base_fields.items():
            v.validate(self.form_data.get(k),k)


class Form(with_metaclass(DeclarativeVariablesMetaclass, BaseForm)):
    pass