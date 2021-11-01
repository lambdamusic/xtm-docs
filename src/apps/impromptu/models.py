from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings
from django import forms
from django.conf.urls.defaults import *	 #for the ajax autocomplete

import datetime
# 
import myutils.modelextra.mymodels as mymodels
# from utils.myutils import blank_or_string, preview_string
# from utils.adminextra.autocomplete_tree_admin import *
# 
from settings import printdebug

EXTRA_SAVING_ACTIONS = True




class FundocEntry(mymodels.EnhancedModel):
	"""(FundocEntry enhanced model - timestamps and creation fields inherited)"""
	
	name = models.CharField(blank=True, max_length=200, verbose_name="name")
	desc = models.TextField(blank=True, verbose_name="desc")
	signature = models.CharField(blank=True, max_length=300, verbose_name="signature")
	examples = models.TextField(blank=True, verbose_name="examples")
	args = models.TextField(blank=True, verbose_name="args")
	returns = models.CharField(blank=True, max_length=300, verbose_name="returns")	
	related = models.CharField(blank=True, max_length=300, verbose_name="related")
	
	class Admin(admin.ModelAdmin):
		list_display = ('id', 'name', 'signature', 'updated_at')
		list_display_links = ('id', 'name',)
		search_fields = ['id', 'name', 'desc']
		list_filter = ('created_at', 'updated_at', 'created_by', 'editedrecord', 'review',)
		#filter_horizontal = (,) 
		#related_search_fields = { 'fieldname': ('searchattr_name',)}
		#inlines = (inlineModel1, inlineModel2)
		fieldsets = [
			('Administration',	
				{'fields':	
					['editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'), 
					  ('updated_at', 'updated_by')
					 ],	 
				'classes': ['collapse']
				}),
			('',	
				{'fields':	
					['name', 'desc', 'signature', 'examples', 'args', 'returns', 'related'
					 ],	 
				# 'classes': ['collapse']
				}),	
			]
		#class Media:
			#js = ("js/admin_fixes/fix_fields_size.js",)
			
		def save_model(self, request, obj, form, change):
			"""adds the user information when the rec is saved"""
			if getattr(obj, 'created_by', None) is None:
				  obj.created_by = request.user
			obj.updated_by = request.user
			obj.save()	
			

	def get_admin_url(self):
		from django.core import urlresolvers
		# TODO: substitute and downcase the path!
		return urlresolvers.reverse('admin:MYAPP_FundocEntry_change', args=(self.id,))
	get_admin_url.allow_tags = True

	def get_databrowse_url(self):
		# TODO: substitute and downcase the path!
		return "/%sdatabrowse/MYAPP/FundocEntry/objects/%s" % (django_settings.URL_PREFIX,self.id)		
	get_databrowse_url.allow_tags = True	


	def get_split_related(self):
		return self.related.split(" ")

	def get_namespace(self):
		temp = self.name.split(":")
		if len(temp) > 1:
			return temp[0] + ":"
		else:
			return ":base"

	@models.permalink
	def get_absolute_url(self):
		return ('impromptu_fun_detail', [str(self.id)])
			
	def save(self, force_insert=False, force_update=False):
		if EXTRA_SAVING_ACTIONS:
			super(FundocEntry, self).save(force_insert, force_update)
			pass
		super(FundocEntry, self).save(force_insert, force_update)	
			
	class Meta:
		verbose_name_plural="FundocEntry"
		verbose_name = "FundocEntry"
		ordering = ["id"]
		
	def __unicode__(self):
		return "FundocEntry %d" % self.id
	




