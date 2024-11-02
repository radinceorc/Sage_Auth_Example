from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from sage_otp.helpers.choices import ReasonOptions

from sage_auth.mixins import (
    ActivateAccountMixin,
    ForgetPasswordConfirmMixin,
    ForgetPasswordDoneMixin,
    ForgetPasswordMixin,
    LoginOtpMixin,
    LoginOtpVerifyMixin,
    PasswordChangeDoneMixin,
    PasswordChangeMixin,
    ReactivationMixin,
    SageLoginMixin,
    UserCreationMixin,
    VerifyOtpMixin,
)

from .forms import (
    OtpLoginForm,
    PasswordResetForm,
    ResetPasswordConfrimForm,
    SageUserCreationForm,
)

User = get_user_model()


class SignUpView(UserCreationMixin):
    form_class = SageUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("verify")
    already_login_url = reverse_lazy("login")


class HomeV(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class OtpVerificationView(VerifyOtpMixin, TemplateView):
    success_url = reverse_lazy("home")
    template_name = "verify.html"

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ForgetPasswordView(ForgetPasswordMixin):
    template_name = "forget-password.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy("auth-otp-verification")

    def get_success_url(self) -> str:
        """Return the success URL for OTP verification."""
        return reverse_lazy("auth-otp-verification")


class ForgetPasswordOTPConfirmView(ForgetPasswordConfirmMixin, TemplateView):
    template_name = "verify_email.html"
    success_url = reverse_lazy("auth-reset-password")
    reason = ReasonOptions.FORGET_PASSWORD


class ForgetPasswordConfirmView(ForgetPasswordDoneMixin):
    template_name = "reset_password.html"
    form_class = ResetPasswordConfrimForm
    success_url = reverse_lazy("login")
    login_url = reverse_lazy("login")


class ActivateAccountView(ActivateAccountMixin):
    success_url = reverse_lazy("login")
    register_url = reverse_lazy("signup")


class CustomLoginView(SageLoginMixin):
    success_url = reverse_lazy("home")
    reactivate_url = reverse_lazy("reactivate")


class ReactivateUserView(ReactivationMixin):
    success_url = reverse_lazy("home")
    template_name = "reactivate.html"


class LoginWithOtpView(LoginOtpMixin):
    form_class = OtpLoginForm
    template_name = "login_otp.html"
    success_url = reverse_lazy("login_v")


class LoginConfrimView(LoginOtpVerifyMixin):
    template_name = "verify_login.html"
    success_url = reverse_lazy("home")


class CustomPasswordChangeView(PasswordChangeMixin):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("password_change_done")


class CustomPasswordChangeDoneView(PasswordChangeDoneMixin):
    template_name = "registration/password_change_done.html"
