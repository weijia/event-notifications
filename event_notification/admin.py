from djangoautoconf.auto_conf_admin_tools.admin_register import AdminRegister
from djangoautoconf.auto_conf_admin_tools.foreign_key_auto_complete import ForeignKeyAutoCompleteFeature
import models

r = AdminRegister()
f = ForeignKeyAutoCompleteFeature()
r.register_all_models(models)

