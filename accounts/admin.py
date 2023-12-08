from django.contrib import admin

from .models import User

class CourseAdmin(admin.ModelAdmin):
    class Meta:
        list_display = 'username','email','modified_date',
        search_fields = ['email',]
        

# Register your models here.
admin.site.register(User,CourseAdmin)
# admin.site.register(CourseAdmin)
