from django.shortcuts import render
from django.http import HttpResponse
from .Form import volunter_form
import razorpay
from .models import Transaction,Transcatid,Course,Solution
from .models import Ticket, SessionRequest, Project, Placement, Jobsupport

def services(request):
    return render(request,'master/service.html')

def session(request):
    return render(request,'master/session.html')

def filltheform(request):
    if request.method=="POST":
        inst=""
        Schoolcollege=""
        username = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        role = request.POST.get('role')
        inst = request.POST.get('inst')
        Schoolcollege = request.POST.get('scname')
        linkedin = request.POST.get('linkedin')
        Abouturself = request.POST.get('abouturself')
        Paymentpath = request.POST.get('paymentgateway')
        qualification = request.POST.get('qualification')
        Session_Request = SessionRequest.objects.create(Name = username,Email = email,
            Mobile = mobile,Role = role,Institute = Schoolcollege,Typeofinst = inst,
            Linkedin = linkedin,Aboutclient = Abouturself,Qualification = qualification,PaymentGateway = Paymentpath)
        Session_Request.save()
        if Paymentpath=="razorpay":
            context = {}
            order_amount = 100
            order_currency = 'INR'
            order_receipt = 'order_rcptid_11'
            notes = {'Shipping address': 'Bommanahalli, Bangalore'}
            client = razorpay.Client(auth=("rzp_live_Iu7wP9i8Wp7Jnf", "4t12rv2a2TzuCuZJJ7LKIJbe"))
            response = client.order.create(dict(amount = order_amount, currency = order_currency, receipt = order_receipt, notes = notes, payment_capture = '0'))
            order_id = response['id']
            order_status = response['status']
            if order_status=='created':
                context['product_id'] = order_amount
                context['price'] = order_amount/100
                context['name'] = username
                context['phone'] = mobile
                context['email'] = email
                context['order_id'] = order_id
                transaction = Transaction.objects.create(made_by = username, amount = order_amount,order_id = order_id)
                transaction.save()
                return render(request, 'master/confirm_order.html', context)
            return HttpResponse('<h1>Error in  create order function</h1>')
        else:
            Amount=100
            return render(request,'master/scan.html',{'amount':Amount})
    else:
        return render(request,'master/filltheform.html')

def payment_status(request):
    response = request.POST
    client = razorpay.Client(auth = ("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    x = response['razorpay_payment_id']
    y = response['razorpay_order_id']
    v = Transcatid.objects.create(order_id = y, transcation_id = x)
    v.save()
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'master/order_summary.html', {'status': 'Payment Successful','x':x,'y':y})
    except:
        return render(request, 'master/order_summary.html', {'status': 'Payment Faliure!!!'})

def mentor(request):
    return render(request,'master/mentor.html')

def mentorform(request):
    if request.method == "POST":
        fm = volunter_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return render(request,'master/mentor-form.html')
        else:
            fm = volunter_form()
            return render(request,'master/mentorform.html',{'fm':fm})
    else:
        fm = volunter_form()
        return render(request,'master/mentorform.html',{'fm':fm})

def startcourse(request):
    return render(request,'master/fillup.html')

def hrcourse(request):
    return render(request,'master/hrcourse.html')

def skilldevelopment(request):
    return render(request,'master/skilldevelopment.html')

def software(request):
    return render(request,'master/software.html')

def courseform(request):
    return render(request,'master/courseform.html')

def paydirect(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname= request.POST.get('lname')
        phone = request.POST.get('mobile')
        email = request.POST.get('email')
        refered = request.POST.get('emaill')
        x = Course.objects.create(name = fname+lname, email = email, mobile = phone, Refered = refered)
        x.save()
        return render(request,'master/scan.html')

def itsolution(request):
    return render(request,'master/itsolution.html')

def itsolutionrequest(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        role = request.POST.get('role')
        inst = request.POST.get('inst')
        Schoolcollege = request.POST.get('scname')
        Abouturself = request.POST.get('tellapp')
        Solution_Request = Solution.objects.create(Name = name, Mobile = phone, Email = email,
                Role = role, Typeofinst = inst, Institute = Schoolcollege, Aboutapp = Abouturself )
        Solution_Request.save()
        return render(request,'master/thank.html')
    else:
        return render(request,'master/solution.html')

def supportnext(request):
    if request.method == 'POST':
        inst=""
        print(request.POST)
        username = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        role = request.POST.get('role')
        inst = request.POST.get('inst')
        Schoolcollege = request.POST.get('scname')
        Abouturself = request.POST.get('abouturself')
        Ticket_request = Ticket.objects.create(Name = username,Email = email,
            Mobile = mobile, Role = role, Typeofinst = inst, Institute = Schoolcollege, AboutTicket = Abouturself)
        Ticket_request.save()
        return render(request,'master/supportnext.html')
    else:
        return render(request,'master/support.html')   

def projectsection(request):
    return render(request,'master/project.html')

def projectrequest(request):
    if request.method=="POST":
        inst=""
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        role = request.POST.get('role')
        inst = request.POST.get('inst')
        Schoolcollege = request.POST.get('scname')
        Abouturself = request.POST.get('tellapp')
        Project_request = Project.objects.create(Name = name, Mobile = phone, Email = email,
            Role = role, Typeofinst = inst, Institute = Schoolcollege, Aboutapp = Abouturself )
        Project_request.save()
        return render(request,'master/thank.html')
    else:
        return render(request,'master/projectform.html')
    
def personalizedsession(request):
    return render(request,'master/personalizedsession.html')

def placementsupportform(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('mobile')
        email = request.POST.get('email')
        inst = request.POST.get('scname')
        yearofpassout = request.POST.get('abouturself')
        qualification = request.POST.get('qualification')
        req = Placement.objects.create(Name = name, Mobile = phone, Email = email,
            Institute = inst, Qualification = qualification, yearofpassout = yearofpassout )
        req.save()
        return render(request,'master/thank.html')
    else:
        return render(request,'master/placementsupportform.html')

def jobsupportform(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('mobile')
        email = request.POST.get('email')
        inst = request.POST.get('scname')
        concern = request.POST.get('abouturself')
        qualification = request.POST.get('qualification')
        req = Jobsupport.objects.create(Name = name, Mobile = phone, Email = email,
             Company = inst, Qualification = qualification, Concern = concern )
        req.save()
        return render(request,'master/thank.html')
    else:
        return render(request,'master/jobsupportform.html')
    
def faq(request):
    return render(request,'master/faq.html')