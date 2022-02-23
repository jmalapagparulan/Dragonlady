from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegistrationForm
from .models import ApplyLoan, ApplyPayment, Registration



def index(request):
    return render (request, 'activities/1_Homepage.html')

def index(request):
    return render (request, 'activities/1_Homepage.html')

def home(request):
    return render (request, 'activities/1_Homepage.html')

def about(request):
    return render (request, 'activities/2_About.html')

def login(request):
    return render (request, 'activities/3_Login.html')



def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('activities/4_Register.html')

    context = {'form':form}
    return render(request,'activities/4_Register.html', context)

def admin_borrower(request):
    registrations = Registration.objects.all()
    return render (request, 'activities/3.1_Admin_Borrower.html', {'registrations':registrations})

def edit(request, borrower_code):
    registration = Registration.objects.get(borrower_code=borrower_code)
    return render (request, 'activities/edit.html', {'registration':registration})

def update(request, borrower_code):
    registration = Registration.objects.get(borrower_code=borrower_code)
    form = RegistrationForm(request.POST, instance=registration)
    if form.is_valid():
        form.save()
        return redirect ('activities/3.1_Admin_Borrower.html')
    return redirect ('activities/3.1_Admin_Borrower.html')

def delete(request, borrower_code):
    registration = Registration.objects.get(borrower_code=borrower_code)
    registration.delete()
    return  HttpResponseRedirect('activities/3.1_Admin_Borrower.html')

def delete1(request, id):
    registration = ApplyLoan.objects.get(id=id)
    registration.delete()
    return  HttpResponseRedirect('activities/3.1_Admin_Loan.html')

def delete2(request, id):
    registration = ApplyPayment.objects.get(id=id)
    registration.delete()
    return  HttpResponseRedirect('activities/3.1_Admin_Payment.html')





def contact_us(request):
    return render (request, 'activities/Footer_Contact_Us.html')

def faqs(request):
    return render (request, 'activities/Footer_FAQs.html')

def sitemap(request):
    return render (request, 'activities/Footer_Sitemap.html')

def privacy_policy(request):
    return render (request, 'activities/Footer_Privacy_Policy.html')

def terms_and_conditions(request):
    return render (request, 'activities/Footer_Terms_and_Conditions.html')

def support(request):
    return render (request, 'activities/Footer_Support.html')

def admin_home(request):
    return render (request, 'activities/3.1_Admin_Home.html')


def admin_loan(request):
    registrations = ApplyLoan.objects.all()
    return render (request, 'activities/3.1_Admin_Loan.html', {'registrations':registrations})


def admin_payment(request):
    registrations = ApplyPayment.objects.all()
    return render (request, 'activities/3.1_Admin_Payment.html', {'registrations':registrations})











def admin_contact_us(request):
    return render (request, 'activities/3.1_Footer_Contact_Us.html')

def admin_faqs(request):
    return render (request, 'activities/3.1_Footer_FAQs.html')

def admin_sitemap(request):
    return render (request, 'activities/3.1_Footer_Sitemap.html')

def admin_privacy_policy(request):
    return render (request, 'activities/3.1_Footer_Privacy_Policy.html')

def admin_terms_and_conditions(request):
    return render (request, 'activities/3.1_Footer_Terms_and_Conditions.html')

def admin_support(request):
    return render (request, 'activities/3.1_Footer_Support.html')

def borrower_home(request):
    return render (request, 'activities/3.2_Borrower_Home.html')

def borrower_account(request):
    return render (request, 'activities/3.2_Borrower_Account.html')

def borrower_loan(request):
    return render (request, 'activities/3.2_Borrower_Loan.html')

def borrower_payment(request):
    return render (request, 'activities/3.2_Borrower_Payment.html')

def borrower_history(request):
    return render (request, 'activities/3.2_Borrower_History.html')

def borrower_contact_us(request):
    return render (request, 'activities/3.2_Footer_Contact_Us.html')

def borrower_faqs(request):
    return render (request, 'activities/3.2_Footer_FAQs.html')

def borrower_sitemap(request):
    return render (request, 'activities/3.2_Footer_Sitemap.html')

def borrower_privacy_policy(request):
    return render (request, 'activities/3.2_Footer_Privacy_Policy.html')

def borrower_terms_and_conditions(request):
    return render (request, 'activities/3.2_Footer_Terms_and_Conditions.html')

def borrower_support(request):
    return render (request, 'activities/3.2_Footer_Support.html')