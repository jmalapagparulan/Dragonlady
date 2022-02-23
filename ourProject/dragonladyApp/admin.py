from django.contrib import admin
from .models import ApplyLoan, ApplyPayment, BorrowerLogin, Registration

# Register your models here.

admin.site.register(Registration),
admin.site.register(BorrowerLogin),
admin.site.register(ApplyLoan),
admin.site.register(ApplyPayment),