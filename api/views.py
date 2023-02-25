from django.shortcuts import render, redirect,HttpResponse
from api.models import *
import pandas as pd
from fuzzywuzzy import fuzz
import random

from django.contrib.auth.decorators import login_required

# Create your views here.

def encode(pk):
    j = random.randint(1001, 9999)
    code = 'Chatbotapi' + str(j) + str(pk)
    return code

def decode(pk):
    code = list(pk)
    pk = str(code[-2]) + str(code[-1])
    return pk

def home(request):
    return render(request,'api/index.html')

def reg(request):

    if request.method == "GET":
        return render(request, 'api/register.html')
    if request.method=="POST":
        Name = request.POST['name']
        Phone = request.POST['phone']
        Email = request.POST['email']
        Gender = request.POST['gender']
        Password = request.POST['password']

        if Registration.objects.filter(Email=Email) or  Registration.objects.filter(Phone=Phone):
            context = {
                'msg' : 'Email or Phone number already Exist'
            }
            return render(request, 'api/register.html',context)

        else:

            Registration.objects.create(Name=Name,Phone = Phone, Email= Email, Gender = Gender, Password = Password)

            return redirect('/login')

def Login(request):
    if request.method == "GET":
        return render(request, 'api/login.html')
    if request.method=="POST":
        Email = request.POST['email']
        Password = request.POST['pass']

        user = Registration.objects.filter(Email = Email).first()
        if user:

            if user.Email == Email and user.Password == Password:
                idd = user.id
                idd = encode(idd)

                return redirect('/dashboard/{}'.format(idd))
            else:
                context = {
                    'msg' : 'Password was Incorrect'
                }
                return render(request,'api/login.html',context)
        else:
            return redirect('/register')


def dashboard(request,pk):
    if len(list(pk)) == 16:
        pk = decode(pk)
        if request.method == "GET":

            name = Registration.objects.filter(id = pk)
            context = {
                'name' : name
            }
            return render(request, 'api/Dashboard.html',context)

        if request.method=="POST":
            bol_values = request.POST.getlist('ai')
            if bol_values[0] == 'Chatbot':

                if FAQ.objects.filter(Idd = pk):
                    pk = encode(pk)
                    return redirect('/update/{}'.format(pk))
                else:
                    pk = encode(pk)
                    return redirect('/faq/{}'.format(pk))

            if bol_values[0] == 'Roomchat':
                return redirect('/secret/')
            else:
                return HttpResponse("Under constraction")
    else:
        return redirect('/login')

# @login_required(login_url='/login')
def faq(request,pk):
    if len(list(pk)) == 16:
        pk = decode(pk)
        if request.method == "GET":

            name = Registration.objects.filter(id = pk)
            context = {
                'name' : name
            }

            return render(request, 'api/faq.html',context)

        if request.method=="POST":
            if FAQ.objects.filter(Idd = pk):
                pk = encode(pk)
                return redirect('/update/{}'.format(pk))
            else:


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
                code = encode(pk)
                context = {
                    'code' : code
                }
                return render(request,'api/code.html',context)
    else:
        return redirect('/login')

def chatbot(request,pk):
    df = pd.DataFrame()
    if request.method == "GET":
        return render(request, 'api/chatbot.html')

    if request.method=="POST":
        pk = decode(pk)

        if FAQ.objects.filter(Idd = pk).first():

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
                    return render(request,'api/chatbot.html',context)
                else:
                    continue

            context = {
                'idd': pk,
                'msg1' : msg,
                'msg' : 'Sorry I cant Understand'
            }
            return render(request,'api/chatbot.html',context)
        else:
            return HttpResponse("Chatbot not available")

def update(request,pk):
    pk = decode(pk)
    if request.method == "GET":
        user = FAQ.objects.filter(Idd=pk)
        context = {
            'user': user
        }
        return render(request, 'api/update.html',context)

    if request.method == "POST":
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

        user = FAQ.objects.filter(Idd=pk)

        for i in user:
            i.qs1 = qs1
            i.qs2 = qs2
            i.qs3 = qs3
            i.qs4 = qs4
            i.qs5 = qs5


            i.ans1 = ans1
            i.ans2 = ans2
            i.ans3 = ans3
            i.ans4 = ans4
            i.ans5 = ans5

            i.save()

        code = encode(pk)
        context = {
            'code': code
        }
        return render(request, 'api/code.html', context)

def delete(request,pk):

    user = FAQ.objects.filter(Idd = pk)
    user.delete()
    pk = encode(pk)
    return redirect('/dashboard/{}'.format(pk))

def Logout(request):
    return render(request,'api/index.html')