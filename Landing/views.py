from django.shortcuts import render ,redirect,get_object_or_404
from Landing.forms import *
from django.http import HttpResponseRedirect
from Landing.models import *

# Create your views here.
def home(request):
	return render(request,"jumbotron.html" , {})

def about(request):
	return render(request,'about.html',{})

def upload(request):
	title = "Welcome"
	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect(instance.get_absolute_url())
	context ={
	"title" : title
	,"form": form
	}

	return render(request,'form.html',context)

def lists(request):
	title = "List"
	query = Post.objects.all().order_by('-timestamp')

	context = {
	'title':title,
	'object' : query
	}
	return render(request,'list.html' , context)

def detail(request,slug=None):
	instance = get_object_or_404(Post,slug=slug)
	context={
	'instance':instance
	}
	return render(request,'detail.html',context)
def update(request,id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect(instance.get_absolute_url())
	context={
	'form':form,
	'title':'Edit'
	}
	return render(request,'form.html',context)



