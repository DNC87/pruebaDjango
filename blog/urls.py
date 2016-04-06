# -*- coding: utf-8 -*-
#!/usr/bin/python –tt

from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
]