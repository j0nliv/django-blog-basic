from django.contrib import admin
from .models import Article,Comment


# Register your models here.


admin.site.register(Comment)

#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author"] 
    search_fields = ["title"] 
    list_display_links = ["title","author"] 
    list_filter = ["created_date"] 
    class Meta:
        model = Article