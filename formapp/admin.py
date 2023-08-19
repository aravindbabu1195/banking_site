from django.contrib import admin
from .models import District,Branch,Material,Registration
# Register your models here.
admin.site.register(Registration)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Material)


