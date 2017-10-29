# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django import forms
# from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tweets.forms import TweetModelForm
from tweets.models import Tweet
from tweets.mixins import FormUserNeededMixin
from django.urls import reverse_lazy


# from myapp.models import Author



# Create your views here.

# CRUD LIST AND RETIRIVE
class TweetCreateView(FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm 
    template_name = "tweets/create_view.html"
    # success_url = reverse_lazy("tweet:detail")
    # login_url = '/admin/'
    # fields = ['user', 'content']

    # def form_valid(self,form):
    # 	if self.request.user.is_authenticated():
	   #  	form.instance.user = self.request.user
	   #  	return super(TweetCreateView,self).form_valid(form)
    #     else:
    #     	form._errors[form.formd.NON_FIELD_ERRORS] = ErrorList(["User Must Be Logged In"])
	   #  	return self.form_invalid(form)

class TweetUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm

    template_name = "tweets/update_view.html"
    success_url = "/tweet/"





class TweetDetailedView(DetailView):
	queryset = Tweet.objects.all()
        template_name = "tweets/detail_view.html"
	
	def get_object(self):
		pk = self.kwargs.get("pk")
		return Tweet.objects.get(id = pk)


class TweetListView(ListView):
	queryset = Tweet.objects.all()
        template_name = "tweets/list_view.html"
	# def get_object(self):
	# 	return Tweet.objects.all()

 

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:list")
    template_name = "tweets/tweet_confirm_delete.html"








# def tweet_detail_view(request, id =1):
# 	obj =  Tweet.objects.get(id = id)
# 	context = { "object" : obj}
# 	return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	context = { "object_list" : queryset}
# 	return render(request, "tweets/list_view.html", context)
