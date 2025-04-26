from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from core.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "description", "is_active", "is_deleted"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save", css_class="btn btn-primary"))
