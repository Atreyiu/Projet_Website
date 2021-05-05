from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['post_title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


    list_display = ('post_title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['post_title']

admin.site.register(Post, PostAdmin)