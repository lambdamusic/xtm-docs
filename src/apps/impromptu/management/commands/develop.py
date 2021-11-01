
##################
#  2015-05-02
#	
#  This script facilitate testing and developing
# 
#  python manage.py develop
# 
#
##################




from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from django.conf import settings
from django.db import connection, models
from django.utils.http import urlquote
from time import strftime
import time, csv

import os

from impromptu.models import *

from settings import printdebug

from bs4 import BeautifulSoup




thisFilePath = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 0)[0] 
LOCAL_DOC_FILE = os.path.join(thisFilePath, 'documentation.plist')






#  helper for django models 
def get_or_new(model, somename):
	"""helper method"""
	try:
		# if there's an object with same name, we keep that one!
		obj = model.objects.get(name=somename)
		print "++++++++++++++++++++++++++ found existing obj:	%s"	 % (obj)
	except:
		obj = model(name=somename)
		obj.save()
		print "======= created new obj:	  %s"  % (obj)
	return obj





# EG:
# bash-3.2$ python manage.py bootstrap_db

class Command(BaseCommand):
	args = '<no args >'
	help = 'bootstrap the db'
	option_list = BaseCommand.option_list  + (
						make_option('--reset', action='store', dest='reset', default='yes',
									help='The _reset_ option removes all previously saved values in the DB'),
				  )

	def handle(self, *args, **options): 
		"""
		args - args 
		options - configurable command line options
		"""

		# feedback:
		print "\n\n++ = ++ = ++ \n%s\nSTARTING:"  % strftime("%Y-%m-%d %H:%M:%S")	
		print "++ = ++ = ++ \n"

		if options['reset'] == 'yes':
			# print "++ = ++ = ++ = ++ Cleaning all previously saved contents ...."
			# Subject.objects.all().delete()
			# print '.........successfully erased all previously saved contents!\n'
			pass # nothing to delete


		if True:			

			# read docs XML file 
			
			# ... arguments
			# ... examples
			# ... long
			# ... related
			# ... returns
			# ... short
			
			soup = BeautifulSoup(open(LOCAL_DOC_FILE))
			
			for x in soup.dict.children:
				if x.name == "key":
					print x.text
					obj = get_or_new(FundocEntry, x.text)
			
				if x.name == "dict":
					for y in x.children:
						if y.name == "key":
						# 	print "...", y.text
							
							if y.text == "arguments":
								temp = y.next_sibling.next_sibling
								stringa = ""
								for z in temp.children: 
									# print z
									if z.name == "key":
										try:
											stringa += "<b>%s</b>:" % z.text
										except:
											pass
									else:
										try:
											stringa += z.text  + "\n"
										except:
											pass
								# print stringa
								obj.args = stringa

							if y.text == "examples":
								temp = y.next_sibling.next_sibling
								stringa = ""
								for z in temp.children: 
									try:
										stringa += z.text  + "\n"
									except:
										pass
								# print stringa
								obj.examples = stringa
								
							if y.text == "long":
								temp = y.next_sibling.next_sibling
								stringa = ""
								for z in temp.children: 
									try:
										stringa += z.text  + "\n"
									except:
										pass
								# print stringa
								obj.desc = stringa
								
							if y.text == "related":
								temp = y.next_sibling.next_sibling
								obj.related = temp.text

							if y.text == "returns":
								temp = y.next_sibling.next_sibling
								obj.returns = temp.text

							if y.text == "short":  # signature
								temp = y.next_sibling.next_sibling
								obj.signature = temp.text
							obj.save()
							
			# print(soup.prettify())

	

		printdebug("\n\n++ = ++ = ++ \nCOMPLETED\n++ = ++ = ++ ")




