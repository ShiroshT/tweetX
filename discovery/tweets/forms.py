from django import forms
from tweets.models import Tweet 

class TweetModelForm(forms.ModelForm):

	class Meta:
		model = Tweet
		fields = [
		   # "user",
		   "content",
		   "location"
		]
		# exclude = ['']