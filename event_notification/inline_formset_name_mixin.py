from django.utils.encoding import force_text


class InlineFormsetNameMixin(object):
    def get_verbose_name(self):
        return force_text(self.__class__._meta.verbose_name)