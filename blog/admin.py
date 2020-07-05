from django.contrib import admin

# Register your models here.
from .models import Post

#admin.site.register(Post)

#display title, post, date as fields in the admin page
"""PostAdmin configures the field display in my admin.

When using class modeling, you must use a decorator. I've organized this PostAdmin to display the title and the body. Also, it includes the date field and it's organized by date published.

"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list_display edits the way the fields are displayed
    list_display = ('title', 'description','body')
    #readonly_fields shows date objects
    readonly_fields = ('date',)
    #date_hierarcy is my sort order
    date_hierarchy = 'date'
    #search_fields adds a search box
    #'title' specifies the field that will be searched
    search_fields = ['title']