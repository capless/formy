from jinja2 import Template

base_field_template = Template(
    """
    {% if errors %}
    {% for error in errors %}
    <p>{{error}}</p>
    {% endfor %}
    {% endif %}
    <input type="{{input_type}}" name="{{name}}" {% if value %}value="{{value}}"{% endif %} {% if css_classes %}class="{{css_classes}}"{% endif %} {% if placeholder %}placeholder={{placeholder}}{% endif %}>
    """
)