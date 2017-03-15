from six import with_metaclass

from .fields import BaseField

import inspect

BUILTIN_DOC_ATTRS = ('_id', '_doc_type')

class DeclaredVars(object):

    base_class = BaseField
    base_field_type = '_base_fields'

    def get_declared_variables(self,bases, attrs):
        properties = {}
        f_update = properties.update
        attrs_pop = attrs.pop
        for variable_name, obj in list(attrs.items()):
            if isinstance(obj, self.base_class):
                f_update({variable_name: attrs_pop(variable_name)})

        for base in bases:
            if hasattr(base, self.base_field_type):
                bft = getattr(base,self.base_field_type)
                if len(bft) > 0:
                    f_update(bft)
        return properties


class DeclarativeVariablesMetaclass(type):
    """
    Partially ripped off from Django's forms.
    http://code.djangoproject.com/browser/django/trunk/django/forms/forms.py
    """
    def __new__(cls, name, bases, attrs):
        attrs['_base_fields'] = DeclaredVars().get_declared_variables(bases, attrs)
        new_class = super(DeclarativeVariablesMetaclass,
                          cls).__new__(cls, name, bases, attrs)

        return new_class


class BaseDocument(object):
    """
    Base class for all Kev Documents classes.
    """
    template_class = None


    def __init__(self, **kwargs):
        self._form = self.process_form_kwargs(kwargs)

    def validate(self):
        pass