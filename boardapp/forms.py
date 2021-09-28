from django import forms
from captcha.fields import CaptchaField

# class PostForm(forms.Form):
#     username=forms.CharField(max_length=20,initial='')
#     pd=forms.CharField(max_length=20,initial='')
#     captcha=CaptchaField()

class PostForm(forms.Form):
    boardsubject=forms.CharField(max_length=100,initial='')
    boardname=forms.CharField(max_length=20,initial='')
    boaradgender=forms.BooleanField()
    boardmail=forms.EmailField(max_length=100,required=False,initial='')
    boardweb=forms.URLField(max_length=100,required=False,initial='')
    boardcontent=forms.CharField(widget=forms.Textarea)
    captcha=CaptchaField()