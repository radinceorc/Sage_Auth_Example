from django.utils.translation import gettext_lazy as _

from sage_auth.forms import (
    SageUserFormMixin,
    ResetPasswordConfrimFormMixin,
    PasswordResetFormMixin,
    OtpLoginFormMixin,
)


class SageUserCreationForm(SageUserFormMixin):
    """Custom form for user creation that extends the SageUserFormMixin."""

    def __init__(self, *args, **kwargs):
        """Customize the form fields, attributes, and validators."""
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({"placeholder": "Enter the pass"})
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Confirm the pass"}
        )


class PasswordResetForm(PasswordResetFormMixin):
    def __init__(self, *args, **kwargs):
        """Customize the form fields, attributes, and validators."""
        super().__init__(*args, **kwargs)


class ResetPasswordConfrimForm(ResetPasswordConfrimFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class OtpLoginForm(OtpLoginFormMixin):
    def __init__(self, *args, **kwargs):
        """Customize the form fields, attributes, and validators."""
        super().__init__(*args, **kwargs)
