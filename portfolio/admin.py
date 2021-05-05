from django.contrib import admin

from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['portfolio_title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


    list_display = ('portfolio_title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['portfolio_title']

admin.site.register(Portfolio, PortfolioAdmin)