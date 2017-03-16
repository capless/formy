from six import with_metaclass
from valley.declarative import DeclaredVars as DV, \
    DeclarativeVariablesMetaclass as DVM

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

    def __init__(self, **kwargs):
        self.uncleaned_data = self.process_form_kwargs(kwargs)

    def __repr__(self):
        return '<{class_name}: {uni} >'.format(
            class_name=self.__class__.__name__, uni=self.__unicode__())

    def __unicode__(self):
        return '({0})'.format(self.__class__.__name__)

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

    def validate(self):
        for k,v in self._base_fields.items():
            v.validate(self.uncleaned_data.get(k),k)




class Form(with_metaclass(DeclarativeVariablesMetaclass, BaseForm)):
    pass