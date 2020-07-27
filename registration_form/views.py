from django.shortcuts import render
from django.http import HttpResponse

from registration_form.models import Register


def registration_form(request):
    # return HttpResponse("<h1> Hello world </h1>")
    # return render(request, 'registration_form/register.html')
    if request.method == 'POST':
        print("in registration")
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        profile_photo = request.POST.get('profile_photo', '')
        email = request.POST.get('email', '')
        gender = request.POST.get('gender', '')
        phone_no = request.POST.get('phone', '')
        address_1 = request.POST.get('address_1', '')
        address_2 = request.POST.get('address_2', '')
        dob = request.POST.get('dob', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pin_code = request.POST.get('pin_code', '')
        user_register = Register(
            name=name,
            surname=surname,
            email=email,
            profile_photo=profile_photo,
            gender=gender,
            phone_no=phone_no,
            address_1=address_1,
            address_2=address_2,
            dob=dob,
            city=city,
            state=state,
            pin_code=pin_code,
        )
        user_register.save()
        done = True
        return render(request, 'registration_form/new_registration.html', {'done': done})
    return render(request, 'registration_form/new_registration.html')
