from django.contrib import admin
from .models import User,Userdata,Book,BookLending
# Register your models here.
admin.site.register(Userdata)
admin.site.register(Book)
admin.site.register(User)
# class BookLendingAdmin(admin.ModelAdmin): 
#     search_fields = ()
# admin.site.register(BookLending , BookLendingAdmin)