from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['tittle','date']
    list_filter = ['date']
    search_fields = ['tittle']
admin.site.register(Post)