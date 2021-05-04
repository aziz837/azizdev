from django.shortcuts import render
import datetime
from django.core.mail import send_mail
from django.conf import settings
from .models import Portfolio


def index(request):
    users = Portfolio.objects.all()
    cnt = {'users': users}
    if request.method=='POST':
        print('okokoko')
        first_name=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        
        date = datetime.date.today()
        sms = str(first_name) + '\n' + str(email) + '\n' + str(phone)+'\n\n' + str(message)+'\n'+str(date)
        send_mail('CONTACT FORM',
                        sms,
                        settings.EMAIL_HOST_USER,
                        ['mubashirov2002@gmail.com'],
                        fail_silently=False)
    
    return render(request, 'index.html', cnt)