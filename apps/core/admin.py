from django.contrib import admin


class AbstractBaseAdmin(admin.ModelAdmin):
    default_list_display = ('created_at',)
    default_search_fields = ('id',)
    search_fields = default_search_fields
    default_read_only_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + self.default_read_only_fields

    def get_list_display(self, request):
        return ('id',) + self.list_display + self.default_list_display

