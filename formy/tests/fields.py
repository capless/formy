import datetime
import unittest
from valley.exceptions import ValidationException

from formy.fields import StringField, SlugField, EmailField, IntegerField, \
    FloatField, BooleanField, DateField, DateTimeField


class FieldsTestCase(unittest.TestCase):

    def test_charfield(self):
        field = StringField(required=True, min_length=1, max_length=20)
        field.validate('String', 'field')
        self.assertRaises(ValidationException, field.validate, 11, 'field')
        self.assertRaises(ValidationException, field.validate, '', 'field')
        self.assertRaises(ValidationException, field.validate, '123456789012345678901234', 'field')
        self.assertRaises(ValidationException, field.validate, None, 'field')
        field = StringField(required=False, min_length=1, max_length=20)
        field.validate(None, 'field')

    def test_slugfield(self):
        field = SlugField(required=True, min_length=1, max_length=20)
        field.validate('some-slug', 'field')
        self.assertRaises(ValidationException, field.validate, 'not a slug', 'field')
        self.assertRaises(ValidationException, field.validate, '', 'field')
        self.assertRaises(ValidationException, field.validate, '123456789012345678901234', 'field')
        self.assertRaises(ValidationException, field.validate, None, 'field')
        field = SlugField(required=False, min_length=1, max_length=20)
        field.validate(None, 'field')

    def test_emailfield(self):
        field = EmailField(required=True, min_length=1, max_length=20)
        field.validate('you@you.com', 'field')
        self.assertRaises(ValidationException, field.validate, 'not a email', 'field')
        self.assertRaises(ValidationException, field.validate, '', 'field')
        self.assertRaises(ValidationException, field.validate, '123456789012345678901234@you.com', 'field')
        self.assertRaises(ValidationException, field.validate, None, 'field')
        field = EmailField(required=False, min_length=1, max_length=20)
        field.validate(None, 'field')

    def test_integerfield(self):
        field = IntegerField(required=True, min_value=1, max_value=20)
        field.validate(1, 'field')
        self.assertRaises(ValidationException, field.validate, 'not a integer', 'field')
        self.assertRaises(ValidationException, field.validate, '', 'field')
        self.assertRaises(ValidationException, field.validate, 100, 'field')
        self.assertRaises(ValidationException, field.validate, None, 'field')
        field = IntegerField(required=False, min_value=1, max_value=20)
        field.validate(None, 'field')

    def test_floatfield(self):
        field = FloatField(required=True, min_value=1, max_value=20)
        field.validate(1.0, 'field')
        self.assertRaises(ValidationException, field.validate, 'not a integer', 'field')
        self.assertRaises(ValidationException, field.validate, '', 'field')
        self.assertRaises(ValidationException, field.validate, 100, 'field')
        self.assertRaises(ValidationException, field.validate, 20.1, 'field')
        self.assertRaises(ValidationException, field.validate, None, 'field')
        field = FloatField(required=False, min_value=1, max_value=20)
        field.validate(None, 'field')

    def test_booleanfield(self):
        field = BooleanField(required=True)
        field.validate(False, 'field')
        field.validate(True, 'field')
        self.assertRaises(ValidationException, field.validate, 11, 'field')
        field = StringField(required=False, min_length=1, max_length=20)
        field.validate(None, 'field')

    def test_datefield(self):
        field = DateField(required=True)
        field.validate(datetime.date(2017, 1, 1), 'field')
        field.validate('2017-01-10', 'field')
        field.validate(datetime.datetime.now(), 'field')
        self.assertRaises(ValidationException, field.validate, 'January 2, 2017', 'field')
        self.assertRaises(ValidationException, field.validate, '', 'field')
        self.assertRaises(ValidationException, field.validate, '10-10-2017', 'field')
        self.assertRaises(ValidationException, field.validate, None, 'field')
        field = DateField(required=False, min_value=1, max_value=20)
        field.validate(None, 'field')

    def test_datetimefield(self):
        field = DateTimeField(required=True)
        field.validate(datetime.datetime.now(), 'field')
        self.assertRaises(ValidationException, field.validate, 'January 2, 2017 10:10:20', 'field')
        self.assertRaises(ValidationException, field.validate, '', 'field')
        self.assertRaises(ValidationException, field.validate, '10-10-2017 10:10:20', 'field')
        self.assertRaises(ValidationException, field.validate, None, 'field')
        field = DateTimeField(required=False)
        field.validate(None, 'field')
