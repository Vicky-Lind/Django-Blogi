from django.contrib import admin

from .models import Postaus

#This makes it so that the admin page shows the Postaus model
#specifically the @admin.register(Postaus) part
@admin.register(Postaus)
class PostausAdmin(admin.ModelAdmin):
    #Makes it so that the admin page shows the title and the time it was created
    list_display = ["otsikko", "luotu"]
    