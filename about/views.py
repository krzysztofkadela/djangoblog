from django.contrib import messages
from django.shortcuts import render, redirect
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST)
        
        # Check if the form is valid
        if collaborate_form.is_valid():
            # If necessary, adjust data here before saving
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your collaboration request has been submitted successfully.')
            return redirect('about')  # Redirect to the 'about' page or desired location

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": CollaborateForm 
        },
    )