from django import forms
from.models import Contact, Newslet,Comment





class ContactForms(forms.ModelForm):


    class Meta:
        model = Contact
        fields = "__all__"


class NewsletForms(forms.ModelForm):


    class Meta:
        model = Newslet
        fields = "__all__"

class CommentForms(forms.ModelForm):


    class Meta:
        model = Comment
        fields = "__all__"



