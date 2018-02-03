from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^words/add_word',views.process),
	url(r'^words/clear',views.clear),     
  ]