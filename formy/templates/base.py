from jinja2 import Template


base_template = Template(
    """
    <ul>
        {% for field in form %}
           <li> {{field.render()}}</li>
        {% endfor %}
        {% if include_submit %}
            <li><input type="submit" value="submit"></li>
        {% endif %}
    </ul>
    """
)