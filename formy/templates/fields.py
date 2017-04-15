from jinja2 import Template

base_field_template = Template(
    """
    {% if error %}
    <div class="alert alert-danger" role="alert">{{error}}</div>
    {% endif %}
    <input type="{{input_type}}" name="{{name}}" {% if value %}value="{{value}}"{% endif %} {% if css_classes %}class="{{css_classes}}"{% endif %} {% if placeholder %}placeholder={{placeholder}}{% endif %}>
    """
)

select_field_template = Template(
    """
    {% if error %}
    <div class="alert alert-danger" role="alert">{{error}}</div>
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
    {% if error %}
    <div class="alert alert-danger" role="alert">{{error}}</div>
    {% endif %}
    <select name="{{name}}" {% if css_classes %}class="{{css_classes}}"{% endif %} multiple>
    {% for k,v in choices.items() %}
        <option value="{{v}}" {% if value == v %}selected{% endif %}>{{k}}</option>
    {% endfor %}
    </select>
    """
)

textarea_field_template = Template(
    """
    {% if error %}
    <div class="alert alert-danger" role="alert">{{error}}</div>
    {% endif %}
    <textarea name="{{name}}" rows="10" cols="30" {% if css_classes %}class="{{css_classes}}"{% endif %} {% if placeholder %}placeholder={{placeholder}}{% endif %}>
    {% if value %}{{value}}{% endif %}
    </textarea>
    """
)

ckeditor_field_template = Template(
    """
    {% if error %}
    <div class="alert alert-danger" role="alert">{{error}}</div>
    {% endif %}
    <textarea name="{{name}}" rows="10" id="id_{{name}}" cols="30" {% if css_classes %}class="{{css_classes}}"{% endif %} {% if placeholder %}placeholder={{placeholder}}{% endif %}>
    {% if value %}{{value}}{% endif %}
    </textarea>
    <script>
                CKEDITOR.replace( 'id_{{name}}' );
            </script>
    """
)
