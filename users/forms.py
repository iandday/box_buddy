# type ignore[misc]
# type ignore[name-defined]

from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import forms as admin_forms
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _

from .models import User


class UserSettingsForm(forms.ModelForm):
    """
    Form for User Settings in the Admin Area.
    To change user settings, see UserAdminChangeForm.
    """

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "photo")
        field_classes = {
            "email": EmailField,
            "first_name": forms.CharField,
            "last_name": forms.CharField,
        }
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id_location_form"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Div(
                Div(
                    "first_name",
                    "last_name",
                    css_class="grid grid-cols-1 md:grid-cols-2 gap-4 py-2",
                ),
                Div(
                    "email",
                ),
            ),
            Div(
                Submit("submit", "Save Profile", css_class="btn btn-primary"),
                Submit("cancel", "Cancel", css_class="btn btn-secondary", onclick="window.history.back();"),
                css_class="w-full mt-2",
            ),
        )


class UserAdminChangeForm(admin_forms.UserChangeForm):  # type ignore[type-arg]
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[attr-defined]
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.UserCreationForm):  # type ignore[type-arg]
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type ignore[name-defined] # type: ignore[attr-defined]
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
