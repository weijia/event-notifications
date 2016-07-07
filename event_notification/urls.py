from django.views.generic import TemplateView

from djangoautoconf.model_utils.url_for_models import add_all_urls
from django.conf.urls import patterns, url, include
import models

urlpatterns = patterns('',
                       url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar_example.html"),
                           name='fullcalendar'),
                       url(r'^schedule/', include('schedule.urls')),
                       )

add_all_urls(urlpatterns, models)
