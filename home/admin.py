from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Platform, PlatformGroup, UserProfile
from django.utils.translation import gettext_lazy as _


# Register your models here.

class ProfileInline(admin.StackedInline):
    # 将UserProfile加入到Admin的user表中
    model = UserProfile
    verbose_name = 'user_profile'
    filter_horizontal = ('platform_groups',)


class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInline,)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.unregister(User)  # 去掉在admin中的注册
admin.site.register(User, UserProfileAdmin)  # 用userProfileAdmin注册user


# Register your models here.
@admin.register(PlatformGroup)
class PlatformGroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('platforms',)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
