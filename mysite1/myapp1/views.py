from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactCreate
from django.http import HttpResponse

from datetime import date

def index(request): #READ
    contactlist = Contact.objects.all()
    return render(request, 'contacts.html', {'contactlist': contactlist })

def upload(request): #CREATE    
    upload = ContactCreate()
    if request.method == 'POST':
        upload = ContactCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form':upload})
    
def update_contact(request, contact_id): #UPDATE
    contact_id = int(contact_id)
    try:
        contact_sel = Contact.objects.get(id = contact_id)
    except Contact.DoesNotExist:
        return redirect('index')
    contact_form = ContactCreate(request.POST or None, instance = contact_sel)
    if contact_form.is_valid():
       contact_form.save()
       return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':contact_form})

def delete_contact(request, contact_id): #DELETE
    contact_id = int(contact_id)
    try:
        contact_sel = Contact.objects.get(id = contact_id)
    except Contact.DoesNotExist:
        return redirect('index')
    
    def calculate_age(date_of_birth):
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return age
    def is_under_18(date_of_birth):
        age = calculate_age(date_of_birth)
        return age < 18
    if is_under_18(contact_sel.date):  # Assuming 'date_of_birth' is the field in your Contact model
        #If the user is under 18, return a 400 Bad Request response with an error message
        return HttpResponse("You cannot delete this contact because you are under 18 years old.")
    
    contact_sel.delete()
    return redirect('index')