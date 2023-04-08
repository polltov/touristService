from django.contrib import admin
from .models import Region, RegionStatistics, Tags, Comments
from django.utils.html import mark_safe


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("title", "rating", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='50' height='50'>")

    get_image.short_description = "Picture"


admin.site.register(RegionStatistics)
admin.site.register(Tags)
admin.site.register(Comments)
