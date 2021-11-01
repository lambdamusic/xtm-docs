from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *
from django.utils.translation import ugettext_lazy as _

from impromptu.models import *

admin.site.register(FundocEntry, FundocEntry.Admin)

