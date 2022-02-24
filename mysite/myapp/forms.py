
from dataclasses import field
from django.forms import ModelForm, Textarea

from .models import Contact, Video, Image

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'message': Textarea(attrs={'cols':40, "rows":10}),
        }

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = "__all__"