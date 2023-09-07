from django.contrib import admin

from .models import VoltageSample


class VoltageSampleAdmin(admin.ModelAdmin):
	list_display = ("timestamp", "voltage", "cell_id",)
	readonly_fields = ("timestamp", "voltage", "cell_id",)

	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	def has_change_permission(self, request, obj=None):
		return False


admin.site.register(VoltageSample, VoltageSampleAdmin)
