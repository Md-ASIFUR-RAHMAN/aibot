from django.shortcuts import render, redirect
from api.models import *
import pandas as pd
from fuzzywuzzy import fuzz
from django.contrib.auth.decorators import login_required

# Create your views here.


def reg(request):

    if request.method == "GET":
        return render(request, 'api/register.html')
    if request.method=="POST":
        Name = request.POST['name']
        Phone = request.POST['phone']
        Email = request.POST['email']
        Gender = request.POST['gender']
        Password = request.POST['password']

        Registration.objects.create(Name=Name,Phone = Phone, Email= Email, Gender = Gender, Password = Password)

        return render(request,'api/login.html')

def Login(request):
    if request.method == "GET":
        return render(request, 'api/login.html')
    if request.method=="POST":
        Email = request.POST['email']
        Password = request.POST['pass']

        user = Registration.objects.filter(Email = Email).first()

        if user.Email == Email and user.Password == Password:
            context = {
                'idd' : user.id
            }
            return render(request, 'api/faq.html',context)
        else:
            return redirect('/login')


@login_required(login_url='/login')
def faq(request,pk):

    if request.method == "GET":
        return render(request, 'api/faq.html')

    if request.method=="POST":
        qs1 = request.POST['qs1']
        qs2 = request.POST['qs2']
        qs3 = request.POST['qs3']
        qs4 = request.POST['qs4']
        qs5 = request.POST['qs5']


        ans1 = request.POST['ans1']
        ans2 = request.POST['ans2']
        ans3 = request.POST['ans3']
        ans4 = request.POST['ans4']
        ans5 = request.POST['ans5']

        FAQ.objects.create(Idd = pk,qs1=qs1,qs2 = qs2, qs3 = qs3, qs4 = qs4, qs5 = qs5 , ans1 = ans1 , ans2 = ans2 , ans3 = ans3, ans4 = ans4, ans5 = ans5)

        context = {
            'code' : pk
        }
        return render(request,'api/code.html',context)

def chatbot(request,pk):
    df = pd.DataFrame()
    if request.method == "GET":
        return render(request, 'api/chatbot.html')

    if request.method=="POST":
        msg = request.POST['msg']

        user = FAQ.objects.filter(Idd = pk).first()

        QS = [user.qs1,user.qs2,user.qs3,user.qs4,user.qs5]
        ANS = [user.ans1,user.ans2,user.ans3,user.ans4,user.ans5]

        df['Question'] = QS
        df['Answer'] = ANS

        print(df)
        for i in range(len(df)):


            f = fuzz.token_sort_ratio(msg, df['Question'][i])

            if f >= 80.0:
                context = {
                    'idd' : pk,
                    'msg1': msg,
                    'msg' : df['Answer'][i]
                }
                print(df['Answer'][i])
                return render(request,'api/chatbot.html',context)
            else:
                continue

        context = {
            'idd': pk,
            'msg1' : msg,
            'msg' : 'Sorry I cant Understand'
        }
        return render(request,'api/chatbot.html',context)


