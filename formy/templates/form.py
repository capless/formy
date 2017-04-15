from jinja2 import Template

table_template = Template(
    """
    <table class="table form">
        {% for field in form %}
        <tr><td><label for="id_{{field.name}}">{{field.get_verbose_name()}}</label></td><td>{{field.render(errors=form._errors)}} {% if field.help_text %}{{field.help_text}}{% endif %}</td></tr>
        {% endfor %}
        {% if include_submit %}
            <tr>
                <td></td><td><input type="submit" value="submit"></td>
            </tr>
        {% endif %}
    </table>
    """
)
ul_template = Template(
    """
    <ul class="ul form">
        {% for field in form %}
           <li> 
                <label for="id_{{field.name}}">{{field.get_verbose_name()}}</label>
                {{field.render(errors=form._errors)}}
                {% if field.help_text %}<span>{{field.help_text}}</span>{% endif %}
            </li>
        {% endfor %}
        {% if include_submit %}
            <li>
                <input type="submit" value="submit">
            </li>
        {% endif %}
    </ul>
    """
)

bootstrap_template = Template(
    """
    {% with form=form %}
    
    {% for field in form %}
        {% if field.input_type != 'checkbox' %}
        <div class="form-group">
        <label for="id_{{field.name}}">{{field.get_verbose_name()}}</label>
        {{field.render(css_classes='form-control',errors=form._errors)}}
        {% if field.help_text %}
        <p class="help-block">{{field.help_text}}</p>
        {% endif %}
        </div>
        {% else %}
         <div class="checkbox">
            <label>
              {{field.render(errors=form._errors)}} {{field.get_verbose_name()}}
            </label>
        </div>
        {% endif %}
  {% endfor %}
    {% if include_submit %}  
      <button type="submit" class="btn btn-default">Submit</button>
    {% endif %}
    {% endwith %}
    """
)