from jinja2 import Template

base_field_template = Template(
    """
    {% if errors %}
    {% for error in errors %}
    <p>{{error}}</p>
    {% endfor %}
    {% endif %}
    <input type="{{input_type}}" name="{{name}}" value="{{value}}" class="{{css_classes}}">
    """
)