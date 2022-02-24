from tkinter import Image
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.core.mail import send_mail

from .forms import ContactForm, ImageForm, VideoForm

# Create your views here.

def index(request):
    if request.method =='POST':
        contactForm = ContactForm(request.POST)
        imageForm = ImageForm(request.POST, request.FILES)
        videoForm = VideoForm(request.POST, request.FILES)

        if imageForm.is_valid():
            imageForm.save()

        if videoForm.is_valid():
            videoForm.save()

        if contactForm.is_valid():
            name = contactForm.cleaned_data['name']
            email = contactForm.cleaned_data['email']
            subject = contactForm.cleaned_data['subject']
            message = contactForm.cleaned_data['message']

            contactForm.save()

            send_mail(subject, message, email, ['bc160404183@vu.edu.pk', email])

            return HttpResponseRedirect('/')

    else:
         contactForm = ContactForm()
         imageForm = ImageForm()
         videoForm = VideoForm()



    return render(request, 'index.html', {'contactForm':contactForm, "imageForm": imageForm, 'videoForm': videoForm})

def display(request):
    images = Image.objects.all()
    videos = videos.objects.all()
    return render(request, 'display.html', {'images': images, 'videos':videos})