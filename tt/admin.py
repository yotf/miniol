from django.contrib import admin

from tt.models import Test,Aktivnost,ZavrseneAktivnosti,Student
admin.site.register(Test)
admin.site.register(Student)
admin.site.register(Aktivnost)
admin.site.register(ZavrseneAktivnosti)

