from django.contrib import admin

from .models import FirstQuarter, SecondQuarter, ThirdQuarter, FourthQuarter, JuniorHigh, Status
from .models import SHFirstQuarter, SHSecondQuarter, SeniorHigh
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Status)


class FirstInline(admin.TabularInline):
    model = FirstQuarter
    extra = 3

class SecondtInline(admin.TabularInline):
    model = SecondQuarter
    extra = 3

class ThirdInline(admin.TabularInline):
    model = ThirdQuarter
    extra = 3

class FourthInline(admin.TabularInline):
    model = FourthQuarter
    extra = 3

@admin.register(JuniorHigh)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("Name", "LRN", "Status")
    inlines = [FirstInline, SecondtInline, ThirdInline, FourthInline]
    list_filter = ("Status",)


class SHFirstInline(admin.TabularInline):
    model = SHFirstQuarter
    extra = 3

class SHSecondtInline(admin.TabularInline):
    model = SHSecondQuarter
    extra = 3


@admin.register(SeniorHigh)
class SHStudentAdmin(admin.ModelAdmin):
    list_display = ("Name", "LRN", "Status")
    inlines = [SHFirstInline, SHSecondtInline]
    list_filter = ("Status",)