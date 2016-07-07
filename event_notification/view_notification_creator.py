# from django.core.exceptions import ImproperlyConfigured
# from django.forms import ALL_FIELDS
# from django.http import HttpResponseRedirect
# from django.utils.encoding import force_text
# from django.views.generic.detail import SingleObjectTemplateResponseMixin, DetailView
from extra_views import UpdateWithInlinesView, CreateWithInlinesView

from djangoautoconf.class_based_views.DetailWithInlineView import DetailWithInlineView


def all_valid(formsets):
    """Returns true if every formset in formsets is valid."""
    valid = True
    for formset in formsets:
        if not formset.is_valid():
            valid = False
    return valid



