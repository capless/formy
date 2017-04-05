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

select_field_template = Template(
    """
    {% if errors %}
    {% for error in errors %}
    <p>{{error}}</p>
    {% endfor %}
    {% endif %}
    <select name="{{name}}" {% if css_classes %}class="{{css_classes}}"{% endif %}>
    {% for k,v in choices.items() %}
        <option value="{{v}}" {% if value == v %}selected{% endif %}>{{k}}</option>
    {% endfor %}
    </select>
    """
)

select_multiple_field_template = Template(
    """
    {% if errors %}
    {% for error in errors %}
    <p>{{error}}</p>
    {% endfor %}
    {% endif %}
    <select name="{{name}}" {% if css_classes %}class="{{css_classes}}"{% endif %} multiple>
    {% for k,v in choices.items() %}
        <option value="{{v}}" {% if value == v %}selected{% endif %}>{{k}}</option>
    {% endfor %}
    </select>
    """
)