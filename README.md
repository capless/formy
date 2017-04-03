# Formy
Python forms library

## Getting Started

Form definition
```python
import formy

class ContactForm(formy.Form):
    name = formy.CharField(required=True,min_length=1,max_length=140)
    email = formy.EmailField(required=True)
    question = formy.CharField(required=True,min_length=10,max_length=500)
```
Form blank instance
```python
>>form = ContactForm()
>>form.render(include_submit=True)
u'\n    <ul>\n        \n           <li> \n    \n    <input type="text" name="question"  >\n    </li>\n        \n           <li> \n    \n    <input type="text" name="name"  >\n    </li>\n        \n           <li> \n    \n    <input type="email" name="email"  >\n    </li>\n        \n        \n            <li><input type="submit" value="submit"></li>\n        \n    </ul>\n    '
>>form.is_valid
False
```
Form instance with kwargs
```python
>>form = ContactForm(name='George',email='george@curious.com',
    question='Where is the man in the yellow hat?')
>>form.render(include_submit=True)
u'\n    <ul>\n        \n           <li> \n    \n    <input type="text" name="name" value="George" >\n    </li>\n        \n           <li> \n    \n    <input type="email" name="email" value="george@curious.com" >\n    </li>\n        \n           <li> \n    \n    <input type="text" name="question" value="Where is the man in the yello hat?" >\n    </li>\n        \n        \n            <li><input type="submit" value="submit"></li>\n        \n    </ul>\n    '
In [ ]:

>>form.is_valid
False
```

### Author

**Twitter:**:[@brianjinwright](https://twitter.com/brianjinwright)
**Github:** [bjinwright](https://github.com/bjinwright)
