from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1_Homepage.html', views.home, name='Homepage'),
    path('2_About.html', views.about, name='About'),
    path('3_Login.html', views.login, name='Login'),



    path('4_Register.html', views.register, name='Register'),
    path('register', views.register, name='Register'),



    path('Footer_Contact_Us.html', views.contact_us, name='Contact Us'),
    path('Footer_FAQs.html', views.faqs, name='FAQs'),
    path('Footer_Sitemap.html', views.sitemap, name='Sitemap'),
    path('Footer_Privacy_Policy.html', views.privacy_policy, name='Privacy Policy'),
    path('Footer_Terms_and_Conditions.html', views.terms_and_conditions, name='Terms and Conditions'),
    path('Footer_Support.html', views.support, name='Support'),
    path('3.1_Admin_Home.html', views.admin_home, name='Admin Homepage'),


    path('3.1_Admin_Borrower.html', views.admin_borrower, name='Admin Borrower'),
    path('edit/<str:borrower_code>', views.edit, name='edit'),
    path('update/<str:borrower_code>', views.update, name="update"),
    path('delete/<str:borrower_code>', views.delete, name='delete'),
    path('delete/activities/3.1_Admin_Borrower.html', views.admin_borrower, name='Admin Borrower'),

    path('delete1/<int:id>', views.delete1, name='delete1'),
    path('delete1/activities/3.1_Admin_Loan.html', views.admin_loan, name='Admin Loan'),

    path('delete2/<int:id>', views.delete2, name='delete2'),
    path('delete2/activities/3.1_Admin_Payment.html', views.admin_payment, name='Admin Payment'),

    path('3.1_Admin_Loan.html', views.admin_loan, name='Admin Loan'),
    path('3.1_Admin_Payment.html', views.admin_payment, name='Admin Payment'),
    path('3.1_Footer_Contact_Us.html', views.admin_contact_us, name='Admin Contact Us'),
    path('3.1_Footer_FAQs.html', views.admin_faqs, name='Admin FAQs'),
    path('3.1_Footer_Sitemap.html', views.admin_sitemap, name='Admin Sitemap'),
    path('3.1_Footer_Privacy_Policy.html', views.admin_privacy_policy, name='Admin Privacy Policy'),
    path('3.1_Footer_Terms_and_Conditions.html', views.admin_terms_and_conditions, name='Admin Terms and Conditions'),
    path('3.1_Footer_Support.html', views.admin_support, name='Admin Support'),
    path('3.2_Borrower_Home.html', views.borrower_home, name='Borrower Homepage'),
    path('3.2_Borrower_Account.html', views.borrower_account, name='Borrower Account'),
    path('3.2_Borrower_Loan.html', views.borrower_loan, name='Borrower Loan'),
    path('3.2_Borrower_Payment.html', views.borrower_payment, name='Borrower Payment'),
    path('3.2_Borrower_History.html', views.borrower_history, name='Borrower History'),
    path('3.2_Footer_Contact_Us.html', views.borrower_contact_us, name='Borrower Contact Us'),
    path('3.2_Footer_FAQs.html', views.borrower_faqs, name='Borrower FAQs'),
    path('3.2_Footer_Sitemap.html', views.borrower_sitemap, name='Borrower Sitemap'),
    path('3.2_Footer_Privacy_Policy.html', views.borrower_privacy_policy, name='Borrower Privacy Policy'),
    path('3.2_Footer_Terms_and_Conditions.html', views.borrower_terms_and_conditions, name='Borrower Terms and Conditions'),
    path('3.2_Footer_Support.html', views.borrower_support, name='Borrower Support'),
]