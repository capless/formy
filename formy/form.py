from six import with_metaclass
from valley.declarative import OrderedDeclaredVars as DV, \
    DeclarativeVariablesMetaclass as DVM
from valley.schema import BaseSchema
from valley.utils import import_util
from .fields import BaseField


class DeclaredVars(DV):
    base_field_class = BaseField


class DeclarativeVariablesMetaclass(DVM):
    declared_vars_class = DeclaredVars


class BaseForm(BaseSchema):
    """
    Base class for all Formy form classes.
    """
    _template = 'formy.templates.ul_template'
    BUILTIN_DOC_ATTRS = []

    def __iter__(self):
        for k, field in self._base_properties.items():
            field.name = k
            field.value = self._data.get(k)
            yield field

    def render(self,include_submit=True):
        template = import_util(self._template)
        return template.render(form=self,include_submit=include_submit)


class Form(with_metaclass(DeclarativeVariablesMetaclass, BaseForm)):
    pass