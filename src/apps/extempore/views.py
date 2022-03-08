from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from functools import reduce
import time
import os

from .models import *
from .management.commands.parse_xtm import XTM_VERSION, XTM_GITHUB_URL

def index(request, page=""):
	
	q = request.GET.get("q", "")

	if page == "extras":
		custom = True
	else:
		custom = False
	
	if q:
		qset = XTMFundocEntry.objects.filter(is_custom=custom, name__icontains=q)		
		items = sorted(qset, key=lambda a: a.get_namespace())
		# namespaces = sorted(list(set([a.get_namespace() for a in qset])))
		namespaces = None
	else:
		qset = XTMFundocEntry.objects.filter(is_custom=custom)			
		items = sorted(qset, key=lambda a: a.get_namespace())
		namespaces = sorted(list(set([a.get_namespace() for a in qset])))	
		
		
	context = {	'items' : items , 
				'q' : q , 
				'namespaces' : namespaces, 
				'XTM_VERSION' : XTM_VERSION, 
				'custom' : custom, 
				'page' : page, 
				}

	return render(request, "extempore/home.html", context)



def funpage(request, permalink):
	"""view that returns a specific function documentation
		if parameter is wrong, gives a 404
	"""
	from django.db.models import Q

	if permalink.endswith(".html"):
		permalink = permalink[:-5]

	item = XTMFundocEntry.objects.get(permalink=permalink)

	if item.is_custom:
		page = "extras"
	else:
		page = "core"

	name = item.name
	if ":" in item.name:
		name = item.name.split(":")[-1]
	name_bits = name.replace("_", " ").split()  # .replace("-", " ")
	

	related_items = XTMFundocEntry.objects.filter(is_custom=item.is_custom).exclude(pk=item.id)
	related_items = related_items.filter(reduce(lambda x, y: x | y, [Q(name__icontains=n) for n in name_bits]))
	
	context = {	'item' : item, 
				'related_items' : related_items, 
				'XTM_VERSION' : XTM_VERSION, 
				'custom' : item.is_custom, 
				'page' : page, 
				}
	
	return render(request, "extempore/item.html", context)
	



def search(request,  page=""):
	"""JS search page
	"""

	allpages = XTMFundocEntry.objects.filter()
	context = {	
		'allpages' : allpages,
		'page' : page
	}
	return render(request, "extempore/search.html", context)
	





