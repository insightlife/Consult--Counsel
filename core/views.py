from django.shortcuts import render
from .models import Donation
from services.models import Transaction
from django.http import HttpResponse
import razorpay

def home(request):
    return render(request,'master/home.html')

def donation(request):
    return render(request,'master/donation.html')

def razorpaygateway(request):
    if request.method == "GET":
        return render(request,'master/razorpaygateway.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        donation = Donation.objects.create(Name = username, Amount=amount, Email=email)
        donation.save()
        return render(request,'master/razorpaygateway.html',{})

def paynext(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount'))
        x=Donation.objects.create(Name = name, Mobileno = phone, Email = email, Amount = amount)
        x.save()
        amount=amount*100
        order_amount = amount
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}
        client = razorpay.Client(auth=("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
        response = client.order.create(dict(amount = order_amount, currency = order_currency, receipt = order_receipt, notes = notes, payment_capture = '0'))
        order_id = response['id']
        order_status = response['status']
        if order_status=='created':
            context['price'] = order_amount/100
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['order_id'] = order_id
            transaction = Transaction.objects.create(made_by = name, amount = order_amount, order_id = order_id)
            transaction.save()
            return render(request, 'master/confirm_order.html', context)
    return HttpResponse('<h1>Error in  create order function</h1>')

def paynow(request):
    return render(request,'master/paynow.html')

def directpaygateway(request):
    if request.method == "GET":
        return render(request, 'master/dp.html')
    else:
        username = request.POST['name']
        mobileno = request.POST['phone']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        x=Donation.objects.create(Name = username, Mobileno = mobileno, Email = email, Amount = amount)
        x.save()
        order_id=username+str(amount)+"dpscan_rt_spl"
        transaction = Transaction.objects.create(made_by = username, amount = amount, order_id = order_id)
        transaction.save()
        return render(request,'master/scan.html',{'amount':amount})

def finalscan(request):
    return render(request,'master/scan.html')

def about(request):
    return render(request,'master/about.html')

def suman(request):
    return render(request,'master/suman.html')

def bhanu(request):
    return render(request,'master/bhanu.html')

def testimony(request):
    return render(request,'master/testimony.html')

def support(request):
    return render(request,'master/support.html')

def privacy(request):
    return render(request,'master/privacy.html')

def policy(request):
    return render(request,'master/policy.html')

def career(request):
    return render(request,'master/career.html')

def job(request):
    fm = digitalform()
    return render(request,'master/job.html',{'fm':fm})

def careerform(request):
    if request.method == "POST":
        return render(request,'master/jobformsubmit.html')
    else:
        return render(request,'master/ok.html')

def joberror(request):
    return render(request,'master/joberror.html')

def mentordetails(request):
    return render(request,'master/mentordetails.html')

def setcookie(request):
    html = HttpResponse("<h1>Welcome to TechVidvan Employee Portal</h1>")
    html.set_cookie('TechVidvan', 'We are setting a cookie', max_age = None)
    return html

def showcookie(request):
    show = request.COOKIES['TechVidvan']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)

