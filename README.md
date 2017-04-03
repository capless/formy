# Formy
Python forms library

[![Build Status](https://travis-ci.org/capless/formy.svg?branch=master)](https://travis-ci.org/capless/formy)

## Getting Started

Form definition
```python
from formy import *

class PersonForm(Form):
    _template = 'formy.templates.form.ul_template'
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    email = EmailField()
    slug = SlugField(required=True,help_text='ex. duke-university')
    
```

####Form blank instance
```python
>>form = PersonForm()
>>form.render(include_submit=True)
u' <ul class="ul form">
        <li><label for="id_first_name">First Name</label> <input type="text" name="first_name" placeholder="First"/>
        </li>
        <li><label for="id_last_name">Last Name</label> <input type="text" name="last_name" placeholder="Last"/></li>
        <li><label for="id_email">Email</label> <input type="email" name="email" placeholder="Email"/></li>
        <li><label for="id_slug">Slug</label> <input type="text" name="slug" placeholder="Slug"/> <span>ex. duke-university</span>
        </li>
        <li><input type="submit" value="submit"/></li>
    </ul>'
>>form.is_valid
False
```
####Form instance with kwargs
```python
>>form_kwargs = {'first_name':'Curious','last_name':'George','email':'curious@george.com','slug':'curious-george'}
>>form = PersonForm(**form_kwargs)
>>form.render(include_submit=True)
u'<ul class="ul form">
        <li><label for="id_first_name">First Name</label> <input type="text" name="first_name" value="Curious"
                                                                 placeholder="First"/></li>
        <li><label for="id_last_name">Last Name</label> <input type="text" name="last_name" value="George"
                                                               placeholder="Last"/></li>
        <li><label for="id_email">Email</label> <input type="email" name="email" value="curious@george.com"
                                                       placeholder="Email"/></li>
        <li><label for="id_slug">Slug</label> <input type="text" name="slug" value="curious-george" placeholder="Slug"/>
            <span>ex. duke-university</span></li>
        <li><input type="submit" value="submit"/></li>
    </ul>'
>>form.is_valid
False
>>form.validate()
>>form.is_valid
True
```

### Author

**Twitter:**:[@brianjinwright](https://twitter.com/brianjinwright)
**Github:** [bjinwright](https://github.com/bjinwright)
