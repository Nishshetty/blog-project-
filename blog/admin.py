from django.contrib import admin
from .models  import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['author','title','text','create_date','published_date','post_images']
    search_fields = ['author','title']
    list_filter = ['author','published_date']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
