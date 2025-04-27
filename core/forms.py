from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from core.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id_location_form"
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save", css_class="btn btn-primary"))
        self.helper.add_input(
            Submit("cancel", "Cancel", css_class="btn btn-secondary", onclick="window.history.back();")
        )
