from django.shortcuts import render
from apps.tables.forms import DateForm
from apps.tables.models import Table
from apps.orders.models import Order
from datetime import date
from django.contrib import messages
from django.core.mail import send_mail

def tables(requests):
    '''Get request show tables for today or checked date.
    Post request make new order and send email.'''
    if requests.method == 'GET':
        context = {}
        context['date'] = date.today().strftime("%Y-%m-%d")

        if requests.GET.get('date', 'no') != 'no':
            context['form'] = DateForm(requests.GET)
            context['date'] = requests.GET.get('date')
        else:
            context['form'] = DateForm()

    else:
        context = {}
        context['date'] = requests.POST.get('date')
        new = Order.objects.create(date=context['date'], name=requests.POST.get('name'), email=requests.POST.get('email'))
        new.save()
        flag = False
        for table in requests.POST.getlist('tables'):
            obj = Table.objects.get(id=table)
            if obj.check_status(context['date']):
                messages.success(requests, 'Table number %s already checked!' % (obj.number,))
            else:
                flag = True
                new.ordered_tables.add(obj)
                new.save()
        if flag:
            send_mail('Subject here', 'Here is the message.', 'from@example.com', [requests.POST.get('email')],
                      fail_silently=False)
            messages.success(requests, 'Thanks! Confirmation email was send.')

        context['form'] = DateForm(requests.GET)

    context.update(prepare_tables(context))
    return render(requests, 'apps/tables/index.html', {'context': context})



def prepare_tables(context):
    '''Check status of tables for date.'''
    context['table_free'] = []
    context['table_checked'] = []

    for table in Table.objects.all():
        if table.check_status(context['date']):
            context['table_checked'].append(table)
        else:
            context['table_free'].append(table)
    return context
