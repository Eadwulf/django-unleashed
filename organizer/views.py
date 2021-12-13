from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLink


def homepage(request):
    template_name = 'organizer/homepage.html'
    return render(request, template_name)

def tag_list(request):
    template_name = 'organizer/tag_list.html'
    context       = {'tag_list': Tag.objects.all()}
    return render(request, template_name, context)

def tag_detail(request, slug):
	if slug == 'create':
		return tag_create(request)
	else:
	    template_name = 'organizer/tag_detail.html'
	    context = {'tag': get_object_or_404(Tag, slug__iexact=slug)}
	    return render(request, template_name, context)

def startup_list(request):
    template_name = 'organizer/startup_list.html'
    context       = {'startup_list': Startup.objects.all()}
    return render(request, template_name, context)

def startup_detail(request, slug):
    template_name = 'organizer/startup_detail.html'
    context = {'startup': get_object_or_404(Startup, slug__iexact=slug)}
    return render(request, template_name, context)

# helper functions
def tag_create(request):
	template_name = 'organizer/tag_form_create.html'
	if request.method == 'POST':
		form = TagForm(request.POST)
	elif request.method == 'GET':
		form = TagForm()
	context = {'form': form}
	return render(request, template_name, context)

def tag_update(request, slug):
	template_name = 'organizer/tag_form_update.html'
	if request.method == 'POST':
		form = TagForm(request.POST)
	elif request.method == 'GET':
		form = TagForm(instance=Tag.objects.get(slug__iexact=slug))
	context = {'slug': slug, 'form': form}
	return render(request, template_name, context)
