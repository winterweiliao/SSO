from django.db import models
from django.contrib.auth.models import AbstractUser, User, ContentType, Group
from django.utils.translation import gettext_lazy as _


class PlatformManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=150, help_text='', verbose_name=_('名称'))
    icon_url = models.TextField(max_length=200, default='', help_text='', verbose_name=_('图标地址'))
    description = models.TextField(max_length=200, help_text='', verbose_name=_('描述'))
    app_url = models.TextField(max_length=200, help_text='', verbose_name=_('平台地址'))
    redirect_url = models.TextField(max_length=200, help_text='', verbose_name=_('跳转地址'))

    objects = PlatformManager()

    class Meta:
        db_table = 'home_platform'
        verbose_name = _('platform')
        verbose_name_plural = _('platforms')

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,


class PlatformGroupManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class PlatformGroup(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)
    platforms = models.ManyToManyField(
        Platform,
        verbose_name=_('platforms'),
        blank=True,
    )
    # users = models.ManyToManyField(
    #     User,
    #     verbose_name=_('users'),
    #     blank=True,
    # )

    objects = PlatformGroupManager()

    class Meta:
        db_table = 'home_platform_groups'
        verbose_name = _('platform_groups')
        verbose_name_plural = _('platform_groups')

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    platform_groups = models.ManyToManyField(
            PlatformGroup,
            verbose_name=_('platform_groups'),
            blank=True,
            help_text=_(
                'The platform_groups this user belongs to. A user will get all platforms '
                'granted to each of their platform_groups.'
            ),
            related_name="user_profile_set",
            related_query_name="user_profile",
        )

    class Meta:
        db_table = 'home_user_profile'
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()


# class UserInfo(AbstractUser):
#     platform_groups = models.ManyToManyField(
#         PlatformGroup,
#         verbose_name=_('platform_groups'),
#         blank=True,
#         help_text=_(
#             'The platform_groups this user belongs to. A user will get all platforms '
#             'granted to each of their groups.'
#         ),
#         related_name="user_set",
#         related_query_name="user",
#     )
#
#     class Meta(AbstractUser.Meta):
#         swappable = 'AUTH_USER_MODEL'
