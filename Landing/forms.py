from django import forms
from Landing.models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields =[
		"title",
		'image',
		'content'
		]
			