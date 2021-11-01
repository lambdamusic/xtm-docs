from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext	#needed for passing the conf details

import time
import os





#
# ===========
# May 3, 2015 : new bootstrap views
# ===========
#


from impromptu.models import *


def index(request):
	
	q = request.GET.get("q", "")
	
	if q:
		qset = FundocEntry.objects.filter(name__icontains=q)		
		items = sorted(qset, key=lambda a: a.get_namespace())
		# namespaces = sorted(list(set([a.get_namespace() for a in qset])))
		namespaces = None
	else:
		qset = FundocEntry.objects.all()			
		items = sorted(qset, key=lambda a: a.get_namespace())
		namespaces = sorted(list(set([a.get_namespace() for a in qset])))	
		
		
	context = {	'items' : items , 'q' : q , 'namespaces' : namespaces}

	return render_to_response("impromptu/home.html", 
								context,
								context_instance=RequestContext(request))



def funpage(request, num):
	"""view that returns a specific function documentation
		if parameter is wrong, gives a 404
	"""
	
	try:
		context = {	'item' : FundocEntry.objects.get(pk=int(num)) }

		return render_to_response("impromptu/item.html", 
									context,
									context_instance=RequestContext(request))
	except:
		# raise Http404
		# return HttpResponseRedirect(reverse('impromptu_home', kwargs={'q': num}))
		return redirect("%s%s" % (reverse('impromptu_home'), "?q=" + str(num)))
		# return HttpResponseRedirect(reverse('impromptu_home', kwargs={'q': num}))







# ===========
# Legacy filesystem based app for viewing source files
# ===========

IMPROMPTU_PATH = "/Users/me/code/impromptu/"
# path component to remove when checking for '.' (see below)
DOT_EXCEPTION_PATH = "michele.pasin/"
IGNORE_FILES = [".DS_Store", ".hgignore", "Icon"]
ALLOWED_FILE_TYPES = ["scm", "txt", "Icon"]



def filebrowser(request):
	""" 
	This view handles requests for all pages, via the template_name variable
	"""

	items = []
	wehave_afile = request.GET.get('file', None) 
	ordering = request.GET.get('ordering', "folder") 
	
	if wehave_afile:
		f = open(wehave_afile)
		context = {	'text' : f.read(), 'filename': wehave_afile}
		f.close()
		return render_to_response("impromptu/filebrowser/fileshow.html", 
									context,
									context_instance=RequestContext(request))
	else:
		path = IMPROMPTU_PATH
		tree = os.walk(path)
		for element in tree:
			dirname = element[0]
			# quick way to remove 
			if "." not in dirname.replace(DOT_EXCEPTION_PATH, ""):
				fileslist = element[2]
				for f in fileslist:
					if not ignore_file(f):
					# if ".DS_Store" not in f:
						fullname = "%s/%s" % (dirname, f)
						modifiedtime = time.strftime("%Y-%m-%d %I:%M:%S %p",time.localtime(os.path.getmtime(fullname)))
						items.append([dirname, f, modifiedtime])
						
		if ordering == "folder":
			pass
		elif ordering == "filename":
			items = sorted(items, key=lambda v: v[1].lower())
		elif ordering == "date":
			items = sorted(items, key=lambda v: v[2], reverse=True)
	
		context = {	'items' : items, }

		return render_to_response("impromptu/filebrowser/index.html", 
									context,
									context_instance=RequestContext(request))




def ignore_file(f):
	for x in ALLOWED_FILE_TYPES:
		if f.endswith(x):
			return False
	return True 



