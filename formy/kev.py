from valley.exceptions import ValidationException

from .form import Form


class KEVForm(Form):
    def __init__(self,_initial=None, **kwargs):
        self._initial = _initial
        kwargs_len = len(kwargs)
        if self._initial:
            self._kev = self._initial
            self._kev._errors = {}
            self._kev._create_error_dict = True
            #HTTP Request == 'GET'
            if kwargs_len == 0:
                kwargs = self._kev._data
            #HTTP Request == 'POST' (someone could send an empty POST but that
            #is what validate is for
            if kwargs_len > 0:
                self._kev._data.update(
                    self._initial.process_schema_kwargs(kwargs))

        else:
            self._kev = self.Meta.document_class(create_error_dict=True)
        super(KEVForm, self).__init__(**kwargs)



    def validate(self):
        super(KEVForm, self).validate()
        if self._is_valid:

            for k,v in self.cleaned_data.items():
                setattr(self._kev,k,v)

            self._kev.validate()
            self._kev.check_unique()


            if len(self._kev._errors.keys()) > 0:
                self._errors.update(self._kev._errors)
                self._is_valid = False

    def save(self):

        self._kev.save()
        self._kev._create_error_dict = False
        return self._kev

    class Meta:
        document_class = None