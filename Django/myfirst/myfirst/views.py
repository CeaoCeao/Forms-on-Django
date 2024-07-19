from django.shortcuts import render, redirect
from django.contrib import messages
from myfirst.models import Insert  # Adjust import based on your actual project structure

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        dod = request.POST.get('dod')
        content = request.POST.get('content')
        author = request.POST.get('author')

        saverecord = Insert(
            name=name,
            dob=dob,
            dod=dod,
            content=content,
            author=author
        )

        saverecord.save()
        
        messages.success(request, 'Obituary submitted successfully.')

        return redirect('submit_obituary')  # Redirecting to the same page after submission

    return render(request, 'obituary_form.html')

