from django.conf.urls import url

from .views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


urlpatterns = [
    url(r'^password/change/$',
        PasswordChangeView.as_view(),
        name='password_change'),

    url(r'^password/reset/$',
        PasswordResetView.as_view(),
        name='password_reset'),

    url(r'^password/reset/done/$',
        PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    url(r'^password/reset/complete/$',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]
