from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView as AuthLoginView,
    PasswordChangeView as AuthPasswordChangeView,
    PasswordResetView as AuthPasswordResetView,
    PasswordResetDoneView as AuthPasswordResetDoneView,
    PasswordResetConfirmView as AuthPasswordResetConfirmView,
    PasswordResetCompleteView as AuthPasswordResetCompleteView,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import TemplateView, View


class LoginView(AuthLoginView):
    template_name = 'authentication/login.html'

    def form_valid(self, *args, **kwargs):
        result = super(LoginView, self).form_valid(*args, **kwargs)
        self.request.user.last_login = timezone.now()
        self.request.user.save()
        return result

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        return next_url or reverse('index')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(
            request,
            'You have sucessfully logged out.'
        )
        return redirect('login')


class PasswordChangeView(AuthPasswordChangeView):
    template_name = 'authentication/password/change.html'
    success_url = reverse_lazy('index')


class PasswordResetView(AuthPasswordResetView):
    email_template_name = 'authentication/password/reset_email.html'
    subject_template_name = 'authentication/password/reset_email_subject.txt'
    template_name = 'authentication/password/reset.html'


class PasswordResetDoneView(AuthPasswordResetDoneView):
    template_name = 'authentication/password/reset_done.html'


class PasswordResetConfirmView(AuthPasswordResetConfirmView):
    template_name = 'authentication/password/reset_confirm.html'


class PasswordResetCompleteView(AuthPasswordResetCompleteView):
    template_name = 'authentication/password/reset_complete.html'
