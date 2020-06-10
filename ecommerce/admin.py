from django.contrib import admin

# Register your models here.


from .models import User, Permission, Roles

"""admin.site.register(SuperAdmin)
admin.site.register(Admin)
admin.site.register(SubAdmin)"""
admin.site.register(User)

admin.site.register(Permission)
admin.site.register(Roles)

