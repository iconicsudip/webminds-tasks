from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from ft.models import Expenses,Balance
from django.contrib.auth.decorators import login_required
from datetime import date
import json
import datetime

# Create your views here.
default_month_date = {
    "01":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "02":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "03":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "04":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "05":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "06":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "07":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "08":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "09":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "10":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "11":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    },
    "12":{
        "01":0,
        "02":0,
        "03":0,
        "04":0,
        "05":0,
        "06":0,
        "07":0,
        "08":0,
        "09":0,
        "10":0,
        "11":0,
        "12":0,
        "13":0,
        "14":0,
        "15":0,
        "16":0,
        "17":0,
        "18":0,
        "19":0,
        "20":0,
        "21":0,
        "22":0,
        "23":0,
        "24":0,
        "25":0,
        "26":0,
        "27":0,
        "28":0,
        "29":0,
        "30":0,
        "31":0
    }
}

def home(request):
    return render(request,'home.html')

def signup(request):
    if (request.method == 'POST'):
        if (request.POST['email'] and request.POST['password1'] and request.POST['password2']):
            if (request.POST['password1'] == request.POST['password2']):
                try:
                    user = User.objects.get(email=request.POST['email'])
                    return render(request, 'signup.html', {'error': "User already exists"})
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=request.POST['email'].split("@")[0],
                        email=request.POST['email'],
                        password=request.POST['password1'],
                    )
                    user.save()
                    today = datetime.date.today()
                    year = today.year
                    current_year_json = {
                        str(year) :default_month_date
                    }
                    balance = Balance(
                        user=user,
                        current_balance=json.dumps(current_year_json)
                    )
                    balance.save()
                    messages.success(request, "Signup Successfully Now You Can Log In")
                    return redirect(signin)
            else:
                return render(request, 'signup.html', {'error': "Password Don't Match"})
        else:
            return render(request, 'signup.html', {'error': "Empty Fields"})
    else:
        return render(request, 'signup.html')

def signin(request):
    if not request.user.is_authenticated:
        if (request.method == 'POST'):
            if (request.POST['email'] and request.POST['password']):
                try:
                    user = User.objects.get(email=request.POST['email'])
                    check_user = auth.authenticate(request,username=user,password =request.POST['password'] )
                    if check_user is not None:
                        auth.login(request, user)
                        messages.success(
                            request, "You are successfully logged in now, you can see your dashboard")
                        return redirect('/')
                    else:
                        messages.error(request, "Invalid Credentials,Please try again")
                        return redirect(signin)
                except User.DoesNotExist:
                    return render(request, 'signin.html', {'error': "User doesnot exists"})
            else:
                return render(request, 'signin.html', {'error': "Empty Fields"})
        else:
            return render(request, 'signin.html')
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect(signin)

def updateJson(json_data,date,amount):
    prev_date = int(date)-1
    if(prev_date>=1 and prev_date<=9):
        prev_date = "0"+str(prev_date)
    else:
        prev_date = str(prev_date)
    if(json_data[date] - json_data[prev_date]<0):
        json_data[date] = json_data[prev_date]+ amount
    else:
        json_data[date] = json_data[prev_date] + (json_data[date] - json_data[prev_date]) + amount
    for i in range(int(date)+1,32):
        key = str(i)
        if(i>=1 and i<=9):
            key = "0"+key
        if(json_data[key]!=0):
            json_data[key]+=amount
    return json_data

@login_required(login_url='/signin/')
def expenses(request):
    if (request.method == 'POST'):
        if (request.POST['date'] and request.POST['month'] and request.POST['option'] and request.POST['amount'] ):
            date = request.POST['date']
            month = request.POST['month']
            option = request.POST['option']
            amount = request.POST['amount']
            if(date.split("-")[0]!=month.split("-")[0]):
                return render(request, 'expences.html', {'error': "Years are not same in date and month fields"})
            else:
                if(date.split("-")[1]!=month.split("-")[1]):
                    return render(request, 'expences.html', {'error': "Months are not same in date and month fields"})
                else:
                    check_amount = float(amount)
                    check_amount = str(check_amount)
                    if(len(check_amount.split(".")[1])>2):
                        return render(request, 'expences.html', {'error': "Amount should have upto two decimal number"})
                    else:
                        # print(date,month,option,amount)
                        user_amount = Balance.objects.get(user=request.user)
                        json_data = json.loads(user_amount.current_balance)
                        if(option=="Credit"):
                            user_amount.total_balance = float(user_amount.total_balance) + float(amount)
                            if(date.split("-")[0] in list(json_data.keys()) == False):
                                json_data[date.split("-")[0]] = default_month_date
                            get_month = json_data[date.split("-")[0]]
                            get_month[date.split("-")[1]] = updateJson(get_month[date.split("-")[1]],date.split("-")[2],float(amount))
                            json_data[date.split("-")[0]] = get_month
                            user_amount.current_balance = json.dumps(json_data)
                            user_amount.save()
                        else:
                            if(float(user_amount.total_balance) - float(amount)<0):
                                return render(request, 'expences.html', {'error': "Have not sufficient balance to debit"})
                            else:
                                user_amount.total_balance = float(user_amount.total_balance) - float(amount)
                                if(date.split("-")[0] in list(json_data.keys()) == False):
                                    json_data[date.split("-")[0]] = default_month_date
                                get_month = json_data[date.split("-")[0]]
                                get_month[date.split("-")[1]] = updateJson(get_month[date.split("-")[1]],date.split("-")[2],-float(amount))
                                json_data[date.split("-")[0]] = get_month
                                user_amount.current_balance = json.dumps(json_data)
                                user_amount.save()
                        expense = Expenses(
                                user = request.user,
                                date = date.split("-")[2],
                                month = month.split("-")[1],
                                year = month.split("-")[0],
                                option = option,
                                amount = amount
                            )
                        expense.save()
                        messages.success(request, "Expenses successfully added")
                        return redirect(expenses)
        else:
            return render(request, 'expences.html', {'error': "Empty Fields"})
    else:
        return render(request,'expences.html')

def getAll(start,end,data_set,recent_balance=None):
    total_credits = 0
    total_debits = 0
    curr_balance = 0
    for i in data_set:
        if(int(i.date)>=start and int(i.date)<=end ):
            if(i.option=="Credit"):
                total_credits+=float(i.amount)
            else:
                total_debits+=float(i.amount)
    if(recent_balance==None):
        return [total_credits,total_debits]
    for i in range(start,end+1):
        key = str(i)
        if(i>=1 and i<=9):
            key = "0"+key
        if(recent_balance[key]!=0):
            curr_balance = float(recent_balance[key])
    return [total_credits,total_debits,curr_balance]

def getMab(today,data_set):
    today = str(today)
    date = int(today.split("-")[2])
    month = today.split("-")[1]
    year = today.split("-")[0]
    result = 0
    get_year_data = data_set.filter(year=year)
    get_month_data = get_year_data.filter(month=month)
    for i in range(1,date+1):
        all_credits = 0
        get_date = str(i)
        if(i>=1 and i<=9):
            get_date = "0"+get_date
        get_date_data = get_month_data.filter(date = get_date)
        for j in get_date_data:
            if(j.option=="Credit"):
                all_credits+=float(j.amount)
        result += all_credits

    return round(result/date,2)

def months(d1, d2,y1,y2):
    return d1 - d2 + 12*(y1 - y2)

@login_required(login_url='/signin/')
def visualize(request):
    balance = Balance.objects.get(user=request.user)
    all_balance = Expenses.objects.filter(user=request.user)
    today = date.today()
    mab = getMab(today,all_balance)
    context = {
        'total_balance':balance.total_balance,
        'monthly_avarage_balance':mab
    }
    if(request.method=="POST"):
        if('month' in request.POST):
            get_month_data = all_balance.filter(month=request.POST['month'].split("-")[1])
            get_year_data = get_month_data.filter(year=request.POST['month'].split("-")[0])
            credits_data = []
            debits_data = []
            current_amounts = []
            get_current_balance_data = Balance.objects.filter(user=request.user)
            for j in range(5):
                start = (7*j)+1
                end = 7*(j+1)
                if(end == 35):
                    end = 31
                json_balance = json.loads(get_current_balance_data.first().current_balance)
                get_year = json_balance[request.POST['month'].split("-")[0]]
                get_month = get_year[request.POST['month'].split("-")[1]]
                data = getAll(start,end,get_year_data,get_month)
                credits_data.append(float(data[0]))
                debits_data.append(float(data[1]))
                current_amounts.append(data[2])

            context["data"] = {
                "credits_data":credits_data,
                "debits_data":debits_data,
                "current_balance":current_amounts
            }
            return render(request,'visualize.html',context)
        elif('month1' in request.POST and 'month2' in request.POST):
            compareMonth = months(int(request.POST['month1'].split("-")[1]),int(request.POST['month2'].split("-")[1]),int(request.POST['month1'].split("-")[0]),int(request.POST['month2'].split("-")[0]))
            get_month_data = all_balance.filter(month=request.POST['month1'].split("-")[1])
            get_year_data = get_month_data.filter(year=request.POST['month1'].split("-")[0])
            get_month_data2 = all_balance.filter(month=request.POST['month2'].split("-")[1])
            get_year_data2 = get_month_data2.filter(year=request.POST['month2'].split("-")[0])
            if(compareMonth==-1 ):
                if(len(get_year_data) and len(get_year_data2)):
                    credits_mon1_data = []
                    credits_mon2_data = []
                    debits_mon1_data = []
                    debits_mon2_data = []
                    get_current_balance_data = Balance.objects.filter(user=request.user)
                    for j in range(5):
                        start = (7*j)+1
                        end = 7*(j+1)
                        if(end == 35):
                            end = 31
                        data = getAll(start,end,get_year_data)
                        credits_mon1_data.append(float(data[0]))
                        debits_mon1_data.append(float(data[1]))
                        data = getAll(start,end,get_year_data2)
                        credits_mon2_data.append(float(data[0]))
                        debits_mon2_data.append(float(data[1]))
                    # print(credits_mon1_data,credits_mon2_data,debits_mon1_data,debits_mon2_data)
                    credit_ratio = []
                    debit_ratio = []
                    for i in range(5):
                        if(int(credits_mon1_data[i])==0 and int(credits_mon2_data[i]==0)):
                            credit_ratio.append("Nothing credited in these week")
                        else:
                            if(int(credits_mon2_data[i]==0) and int(credits_mon1_data[i]!=0)):
                                credit_ratio.append("Nothing credited in this week")
                            elif(int(credits_mon1_data[i]==0) and int(credits_mon2_data[i]!=0)):
                                credit_ratio.append("Nothing credited in previous week")
                            else:
                                credit_ratio.append(round(credits_mon1_data[i]/credits_mon2_data[i],2))
                    for i in range(5):
                        if(int(debits_mon1_data[i])==0 and int(debits_mon2_data[i]==0)):
                            debit_ratio.append("Nothing debited in these week")
                        else:
                            if(int(debits_mon2_data[i]==0) and int(debits_mon1_data[i]!=0)):
                                debit_ratio.append("Nothing debited in this week")
                            elif(int(debits_mon1_data[i]==0) and int(debits_mon2_data[i]!=0)):
                                debit_ratio.append("Nothing debited in previous week")
                            else:
                                debit_ratio.append(round(debits_mon1_data[i]/debits_mon2_data[i],2))
                    # print(credit_ratio,debit_ratio)
                    context['ratio'] = {
                        'credit_ratio':credit_ratio,
                        'debit_ratio':debit_ratio
                    }
                    return render(request,'visualize.html',context)
                else:
                    context['error'] = "Select existing months"
                    return render(request,'visualize.html',context)
            else:
                context['error'] = "Select only consecutive months (e.g : May and June or March and April)"
                return render(request,'visualize.html',context)
        else:
            context['error'] = "Please enter month"
            return render(request,'visualize.html',context)
    else:
        return render(request,'visualize.html',context)
