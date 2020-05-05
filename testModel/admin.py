from django.contrib import admin
from testModel.models import Test,Contact,Tag

class TagInline(admin.TabularInline):
    model =Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') 
    search_fields = ('name',)
    inlines =[TagInline]
    # fields = ("name","email")
    fieldsets =(
        ["Main",{
            "fields":("name","email"),
        }],
        ["Advance",{
            "classes":("collapse",),
            "fields":("age",),
        }],
    )


admin.site.register(Contact,ContactAdmin)
admin.site.register([Test,Tag])