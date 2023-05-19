from django.contrib import admin
from .models import Delhi,Contact,Mumbai,Chennai,Surat
from mapwidgets.widgets import GooglePointFieldInlineWidget
from django.contrib.gis.db.models import GeometryField
# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    ...
    formfield_overrides = {
        GeometryField: {"widget": GooglePointFieldInlineWidget}
    }
admin.site.register(Delhi,PlaceAdmin)
admin.site.register(Contact)
admin.site.register(Mumbai,PlaceAdmin)
admin.site.register(Chennai,PlaceAdmin)
admin.site.register(Surat,PlaceAdmin)
