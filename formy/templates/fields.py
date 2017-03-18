from jinja2 import Template

base_field_template = Template(
    """
    <input type="{{input_type}}" name="{{name}}" value="{{value}}" class="{{css_classes}}">
    """
)