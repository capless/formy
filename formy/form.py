from valley.declarative import DeclaredVars as DV, \
    DeclarativeVariablesMetaclass as DVM
from valley.schema import BaseSchema

from .fields import BaseField
from .utils import temp_env


class DeclaredVars(DV):
    base_field_class = BaseField


class DeclarativeVariablesMetaclass(DVM):
    declared_vars_class = DeclaredVars


class BaseForm(BaseSchema):
    """
    Base class for all Formy form classes.
    """
    _template = 'formy/form/ul.html'
    BUILTIN_DOC_ATTRS = []
    _create_error_dict = True

    def __iter__(self):
        for k, field in self._base_properties.items():
            field.name = k
            field.value = self._data.get(k)
            yield field

    def render(self, include_submit=True):
        return temp_env.get_template(self._template).render(
            form=self, include_submit=include_submit)

    def render_static_assets(self):
        static_assets = []
        for field in self:
            static_assets.extend(field.static_assets)
        return ''.join(set(static_assets))


class Form(BaseForm, metaclass=DeclarativeVariablesMetaclass):
    pass
