from django.contrib.auth.models import User
from extra_views import CreateWithInlinesView
from schedule.models import Event
import django.db.models as models
from extra_views import InlineFormSet

from djangoautoconf.class_based_views.detail_with_inline_view import DetailWithInlineView
from event_notification.inline_formset_name_mixin import InlineFormsetNameMixin


def get_verbose_name(self):
    return models.force_text(self.Meta.verbose_name)


def get_event_class(model_class):
    event_class = type("%s%s" % (model_class.__name__, "Notification"),
                       (Event, InlineFormsetNameMixin), {
                           "last_modifier": models.ForeignKey(User, null=True, blank=True),
                           "item": models.ForeignKey(model_class),
                           # "get_verbose_name": get_verbose_name,
                       })
    return event_class


class NotificationFactory(object):
    fields = None
    extra = 1

    def __init__(self, model_class, event_class=None, inline_class=None):
        super(NotificationFactory, self).__init__()
        self.model_class = model_class
        self.event_class = event_class
        self.inline_class = inline_class

    def get_inline_class(self):
        fields = self.fields or ["start", "end", "title", "description"]
        event_class = self._get_event_model_class()
        inline_class = type("%s%s" % (event_class.__name__, "Inline"),
                            (InlineFormSet, ), {
                                # "Meta": type("Meta", (), {"model": self.model_class, "fields": []}),
                                "model": event_class,
                                "extra": self.extra,
                                "fields": fields
                            })
        return inline_class

    def _get_event_model_class(self):
        if self.event_class is not None:
            return self.event_class
        return get_event_class(self.model_class)

    def get_notification_create_view(self):
        base_view_name = "CreateView"
        base_class = CreateWithInlinesView

        return self.get_view(base_class, base_view_name)

    def get_notification_update_view(self):
        base_view_name = "UpdateView"
        base_class = DetailWithInlineView

        return self.get_view(base_class, base_view_name)

    def get_view(self, base_view_name, base_class):
        inline_class = self.inline_class or self.get_inline_class()
        # fields = self.fields or ["start", "end", "title", "description"]
        create_view = type("%s%s" % (self.model_class.__name__, base_view_name), (base_class,),
                           {
                               "model": self.model_class,
                               "inlines": [inline_class],
                               "template_name": "event_notification/view_notification.html",
                               # "fields": fields
                           })
        return create_view
