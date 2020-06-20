# mortgage.py
#
# Exercise 1.7
def mortgage_calculator(principal, rate, payment, extra_payment_start_month, extra_payment_end_month, extra_payment):

    months = 0
    total_paid = 0.0

    while principal > 0:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        months += 1

        if months >= extra_payment_start_month and months <  extra_payment_end_month:
            principal = principal - extra_payment
            total_paid = total_paid + extra_payment

        if principal < 0:
            total_paid = total_paid + principal
            principal = principal - principal

        print(months, round(total_paid,2), round(principal,2))

    print(f'Total paid: ${total_paid:0.2f}')
    print(f'Total months: {months}')

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
principal = 500000.0
rate = 0.05
payment = 2684.11

mortgage_calculator(principal,rate, payment, extra_payment_start_month, extra_payment_end_month, extra_payment)
