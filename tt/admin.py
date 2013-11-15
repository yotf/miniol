from django.contrib import admin

from tt.models import Aktivnost,ZavrseneAktivnosti,Student,Module

admin.site.register(Student)
admin.site.register(Aktivnost)
admin.site.register(ZavrseneAktivnosti)
admin.site.register(Module)
