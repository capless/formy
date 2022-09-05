from valley.declarative import DeclaredVars as DV, \
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
    _create_error_dict = True

    def __iter__(self):
        for k, field in self._base_properties.items():
            field.name = k
            field.value = self._data.get(k)
            yield field

    def render(self,include_submit=True):
        template = import_util(self._template)
        return template.render(form=self,include_submit=include_submit)

    def render_static_assets(self):
        static_assets = []
        for field in self:
            static_assets.extend(field.static_assets)
        return ''.join(static_assets)


class Form(BaseForm, metaclass=DeclarativeVariablesMetaclass):
    pass