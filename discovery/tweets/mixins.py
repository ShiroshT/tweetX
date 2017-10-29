from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.utils import ErrorList




class FormUserNeededMixin(object):

    def form_valid(self,form):
    	if self.request.user.is_authenticated():
	    	form.instance.user = self.request.user
	    	return super(FormUserNeededMixin,self).form_valid(form)
        else:
        	form._errors[form.formd.NON_FIELD_ERRORS] = ErrorList(["User Must Be Logged In"])
	    	return self.form_invalid(form)
