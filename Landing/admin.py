from django.contrib import admin
from Landing.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ["title" , 
	"image",
	"content",
	"updated",
	"timestamp",
	 "id"]
	class Meta:
		model = Post

admin.site.register(Post,PostAdmin)
