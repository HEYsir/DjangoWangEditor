from django.conf.urls import url
from .views import uploadFile

import os
from django import views
from django.conf import settings
STATIC_ROOT = os.path.join(settings.BASE_DIR, 'DjangoWangEditor/static/editor')
MEDIA_ROOT = settings.MEDIA_ROOT

urlpatterns = [
	url(r'^static/(?P<path>.*)$', views.static.serve, {'document_root': STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': MEDIA_ROOT}),
	url(r'upload/', uploadFile),
]