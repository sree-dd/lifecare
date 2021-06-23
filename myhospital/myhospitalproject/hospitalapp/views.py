from email import message

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, redirect

from departmentapp.models import Doctor, Department


# Create your views here.

def index(request):
    doc = Doctor.objects.all()
    paginator = Paginator(doc, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        doctors = paginator.page(page)
    except(EmptyPage, InvalidPage):
        doctors = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'doctor': doc})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('patient')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                message.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                message.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                print("user created")
                return redirect('login')
        else:
            print("password not matched")
            message.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def patient(request):
    return render(request, "patient.html")


def addappointment(request):
    department1 = Department.objects.all()
    doctor1 = Doctor.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        department = request.POST['department']
        doctor = request.POST['doctor']


        return render(request, "thankyou.html",
                      {'name': name,'address' : address, 'phone': phone, 'date': date, 'time': time, 'department': department,
                       'doctor': doctor,})

    return render(request, "appointment.html", {'doctor':doctor1, 'department': department1})


def thankyou(request):
    return render(request, "thankyou.html")


def detail(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "detail.html", {'doctor': doctor})


