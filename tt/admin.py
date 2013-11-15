from django.contrib import admin

from tt.models import Test,Aktivnost,ZavrseneAktivnosti,Student,Module
admin.site.register(Test)
admin.site.register(Student)
admin.site.register(Aktivnost)
admin.site.register(ZavrseneAktivnosti)
admin.site.register(Module)
