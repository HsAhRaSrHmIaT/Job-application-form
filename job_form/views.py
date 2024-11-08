from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            occupation = form.cleaned_data['occupation']
            # print(name, email, phone, message, occupation)

            Form.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
                occupation=occupation
            )
            message_body = f"A new job application has been submitted.\n\nThank you, {name.split()[0]}!" \
                           f"\n\nPlease do not reply to this email.\n\nRegards,\nAdmin."
            email = EmailMessage(
                'New Job Application',
                message_body,
                to=[email]
            )
            email.send()

            messages.success(request, 'Your application has been submitted successfully.')
            return redirect('index')

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')