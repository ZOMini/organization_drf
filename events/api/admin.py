
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from api.forms import UserChangeForm, UserCreationForm
from api.models import Event, Organization, OrganizationInEvent, User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email', 'id', 'is_admin', 'is_active', 'organization']
    list_filter = ['organization']
    fieldsets = [
        (None, {'fields': ['email', 'organization']}),
        ('Permissions', {'fields': ['is_admin']}),
    ]
    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['email', 'organization', 'password1', 'password2'],
            },
        ),
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'address', 'postcode', 'members']
    list_filter = ['title']
    search_fields = ['title']
    ordering = ['title']

    def members(self, obj):
        return [i.email for i in User.objects.filter(organization=obj).all()]
    members.short_description = 'Участники от компании.'


class OrganizationInline(admin.TabularInline):
    model = OrganizationInEvent
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = (OrganizationInline,)
    list_display = ['id', 'title', 'description', 'date', 'company', 'image_tag']
    list_filter = ['date']
    search_fields = ['title']
    ordering = ['date']

    def company(self, obj):
        return [i.organization for i in OrganizationInEvent.objects.filter(event=obj).all()]
    company.short_description = 'Участвующие компании'
