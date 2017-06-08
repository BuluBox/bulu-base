from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from bulu.authentication.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('bulu.authentication.urls')),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
]

if settings.DEBUG:
    from django.views.static import serve
    import debug_toolbar

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),

        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
