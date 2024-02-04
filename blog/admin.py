from django.contrib import admin

# Register your models here.
from .models import BlogCategory, Post, BlogTag

# admin.site.register(BlogCategory)
# admin.site.register(BlogTag)
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title',"is_active")
    # list_filter = ('status', 'created_on')
    # search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}
    # date_hierarchy = 'created_on'


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass
