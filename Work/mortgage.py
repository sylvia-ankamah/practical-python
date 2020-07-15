# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0
months=0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months=months + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if (months>=extra_payment_start_month)and(months<=extra_payment_end_month):
        principal=principal - 1000
        total_paid=total_paid+1000

    if principal<0:
        total_paid= total_paid + principal
        principal = 0
    print(months, total_paid, principal)

print(months, total_paid, principal)

    
        

print(months, total_paid, principal)

print('Total paid', total_paid)
print('total months', months)