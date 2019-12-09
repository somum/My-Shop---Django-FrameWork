from django.contrib import admin

# Register your models here.
from .models import product,Contact,user,userInformation

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(user)
admin.site.register(userInformation)

