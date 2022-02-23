from distutils.command.upload import upload
from email.policy import default
from django.db import models

#Registration (Create Account)
class Registration (models.Model):
    gender = [
        ('M','Male'),
        ('F','Female'),
        ('NB','Non-Binary'),
        ('T','Transgender'),
        ('I','Intersex'),
        ('IPNTS','I prefer not to say'),
    ]

    first_name = models.CharField (max_length=50, blank=False, verbose_name="first_name")
    middle_name = models.CharField (max_length=50, blank=True, verbose_name="middle_name")
    surname = models.CharField (max_length=50, blank=False, verbose_name="surname")
    age = models.IntegerField (blank=False, verbose_name="age")
    birthday = models.DateField (blank=False, verbose_name="birthday")
    gender = models.CharField (max_length=50, choices=gender, default="Male", verbose_name="gender")
    email_address = models.EmailField (max_length=50, blank=False, verbose_name="email_address")
    home_address = models.CharField (max_length=50, blank=False, verbose_name="home_address")
    borrower_code = models.CharField (max_length=4, primary_key=True, unique=True, verbose_name="borrower_code")
    valid_id = models.ImageField (upload_to="D:\SchoolWorks\CPET12L\WebApp\ourProject\Image Files\Valid ID", blank=False, verbose_name="valid_id")

    class Meta:
        db_table = "dragonladyApp_Registration"

#Login (Borrower Code)
class BorrowerLogin (models.Model):
    borrower_code = models.ForeignKey (Registration, on_delete=models.CASCADE)


#Borrower (Loan-making)
class ApplyLoan (models.Model):
    mode_of_loan_transfer = [
            ('GC','Gcash'),
            ('PM','Paymaya'),
            ('PP','Paypal'),
            ('BDO','BDO'),
            ('WI','Walk-In'),
        ]

    id = models.AutoField(primary_key=True)
    borrower_code = models.ForeignKey (Registration, on_delete=models.CASCADE)
    loan_date = models.DateField (blank=False, verbose_name="loan_date")
    amount_of_loan = models.IntegerField (blank=False, verbose_name="amount_of_loan")
    to_be_paid = models.IntegerField (blank=False, verbose_name="to_be_paid")
    due_date = models.DateField (blank=False, verbose_name="due_date")
    mode_of_loan_transfer = models.CharField (max_length=50, blank=False, choices=mode_of_loan_transfer, default="Gcash", verbose_name="mode_of_loan_transfer")

 

#Borrower (Payment-making)
class ApplyPayment (models.Model):
    mode_of_payment = [
                ('GC','Gcash'),
                ('PM','Paymaya'),
                ('PP','Paypal'),
                ('BDO','BDO'),
                ('WI','Walk-In'),
            ]

    id = models.AutoField(primary_key=True)
    borrower_code = models.ForeignKey (ApplyLoan, on_delete=models.CASCADE)
    payment_date = models.DateField (blank=False, verbose_name="payment_date")
    to_be_paid = models.IntegerField (blank=False, verbose_name="to_be_paid")
    amount_paid = models.IntegerField (blank=False, verbose_name="amount_paid")
    remaining_balance = models.IntegerField (blank=False, verbose_name="remaining_balance")
    mode_of_payment = models.CharField (max_length=50, blank=True, choices=mode_of_payment, default="Gcash", verbose_name="mode_of_payment")
    proof_of_payment = models.ImageField (upload_to="D:\SchoolWorks\CPET12L\WebApp\ourProject\Image Files\Proof of Payment", blank=True, verbose_name="proof_of_payment")

