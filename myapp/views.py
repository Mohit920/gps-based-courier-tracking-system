from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User,New_order

login_detail={
            'status':'Login',
            'username':' ',
            'error':' '
            }
order_detail = {
    'ref_id':'',
    'name':'',
    'location':'',
    'ordered_date':'',
    'shipment_date':'',
    'phone':'',
    'email':'',
    'from':'',
    'to':'',
    'weight':'',
    'cost':'',
    
}

# Create your views here.
def login(request):
    # registering user in database
    if(request.method =='POST'):
        # registeration processing code
        if request.POST.get('full_name') and request.POST.get('email') and request.POST.get('password'):
            data= User()
            data.full_name = request.POST.get('full_name')
            data.email = request.POST.get('email')
            data.password = request.POST.get('password')
            data.save()
            login_detail['username'] = request.POST.get('fullname')
            
            return render(request,"index.html",login_detail)

            # login processing code
        if request.POST.get('email') and request.POST.get('password'):
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.all()
            for x in user:
                if x.email == email and x.password == password:
                    login_detail['status'] = 'Logout'
                    login_detail['username'] = x.full_name 
                    return render(request,'index.html',login_detail)
                
    return render(request,'login.html',login_detail)

flag =0
def index(request):
    if request.method == 'POST':
        if request.POST.get('Order') and request.POST.get('Waybill') and request.POST.get('agree'):
            a = request.POST.get('Order')
            a = a.strip()
            new_order = New_order.objects.all()
            for x in new_order:
                if x.id == a:
                    order_detail['ref_id']=a
                    order_detail['name']=x.name
                    order_detail['location']=x.location
                    order_detail['shipment_date']=x.shipment_date
                    order_detail['ordered_date'] = x.ordered_date
                    order_detail['phone']=x.contact
                    order_detail['email']=x.email
                    order_detail['from']=x.source
                    order_detail['to']=x.destination
                    order_detail['weight']=x.weight
                    order_detail['cost']=x.cost
                    flag = 1;
                else:
                    continue

            if flag ==1:
                flag =0
                return render(request,'track.html',order_detail)
            else:
                login_detail['error']='Invalid Tracking  ID, Try again'
                return render(request,'index.html',login_detail)

    return render(request,'index.html',login_detail)

def contact(request):
    return render(request,'contact.html',login_detail)



def about(request):
    return render(request,'about.html',login_detail)



def track(request):

    if request.method == 'POST':
        if request.POST.get('refno'):
            new_order = New_order.objects.all()
            a =request.POST.get('refno')
            a= a.strip()
            for x in new_order:
                if x.id == a:
                    order_detail['ref_id']=a
                    order_detail['name']=x.name
                    order_detail['location']=x.location
                    order_detail['shipment_date']=x.shipment_date
                    order_detail['ordered_date'] = x.ordered_date
                    order_detail['phone']=x.contact
                    order_detail['email']=x.email
                    order_detail['from']=x.source
                    order_detail['to']=x.destination
                    order_detail['weight']=x.weight
                    order_detail['cost']=x.cost
                    flag = 1;
                else:
                    continue

            if flag ==1:
                flag =0
                return render(request,'track.html',order_detail)
            else:
                login_detail['error']='Invalid Tracking  ID, Try again'
                return render(request,'track.html',login_detail)
    
    return render(request,'track.html',login_detail)

transaction_detail={
    'id':'',
    'cost':''
}
def send_courier(request):
    if request.method == 'POST':
        
        if request.POST.get('fullname') and request.POST.get('contactno') and  request.POST.get('email') and request.POST.get('pickupdate') and request.POST.get('address') and request.POST.get('from-location') and request.POST.get('to-location') and request.POST.get('weight'):
           
            obj = New_order()
            obj.name = request.POST.get('fullname')
            obj.email =  request.POST.get('email')
            obj.contact = request.POST.get('contactno')
            obj.source = request.POST.get("from-location")
            obj.destination = request.POST.get('to-location')
            obj.weight = request.POST.get('weight')
            obj.address = request.POST.get('address')
            obj.date = request.POST.get('pickupdate')
            obj.cost= 800
            transaction_detail['id'] = obj.id
            transaction_detail['cost'] = obj.cost
            obj.save()
           
            return render(request,'send-courier.html',transaction_detail)

    return render(request,'send-courier.html')