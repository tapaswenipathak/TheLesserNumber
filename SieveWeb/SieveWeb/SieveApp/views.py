from django.shortcuts import render, redirect
from .models import ContactFormModel
from .forms import ContactForm

def contact_page(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        obj = ContactFormModel() 
        obj.name = form.cleaned_data.get('name')
        obj.email = form.cleaned_data.get('email')
        obj.message = form.cleaned_data.get('message')
        obj.save()
        return redirect('/')
    context = {
        "form": form
    }   
    return render(request,'contact/contact.html', context)
