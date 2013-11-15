from django.contrib import admin

from tt.models import Aktivnost,ZavrseneAktivnosti,Student,Module

admin.site.register(Student)
#admin.site.register(Aktivnost)
admin.site.register(ZavrseneAktivnosti)
#admin.site.register(Module)

class AktivnostInline(admin.TabularInline):
    model = Aktivnost
    extra = 2


class ModuleAdmin(admin.ModelAdmin):
    fieldset = [
        (None, {'fields':['title']}),
        ]
    inlines = [AktivnostInline]


admin.site.register(Module,ModuleAdmin)